#!/bin/bash

ALGO_PATH=$1
CONFIG_FILE=$2
DIR_TEST=$3
DIR_RESULT=$4
NUMA_CONSTRAINT=1

if [ $# -ne 4 ]
then
    echo "Invalid number of arguments"
    echo "Example: ../build/algo ../algo/config.cfg <directory_with_tests> <directory_for_results>"
    exit 127
fi

declare -a pids

TESTS=$(ls -1 $DIR_TEST | grep dcxml | sed -e 's/\.dcxml$//')

# for dots in float in seq instead commas
LANG=en_US

for test in $TESTS
do
    i=0
    for vm_exhaustive in $(seq 0 1 1)
    do
        for numa_exhaustive in $(seq 0 1 1)
        do
            NEW_CONFIG_FILE=$CONFIG_FILE"_"$test"_"$vm_exhaustive"_"$numa_exhaustive
            cp $CONFIG_FILE $NEW_CONFIG_FILE
            sed -i "s/^\(vm_exhaustive\s*=\s*\).*\$/\1$vm_exhaustive/" $NEW_CONFIG_FILE
            sed -i "s/^\(numa_exhaustive\s*=\s*\).*\$/\1$numa_exhaustive/" $NEW_CONFIG_FILE
            sed -i "s/^\(numa_constraint\s*=\s*\).*\$/\1$NUMA_CONSTRAINT/" $NEW_CONFIG_FILE
            echo $ALGO_PATH $DIR_TEST"/"$test".dcxml" $DIR_RESULT"/"$test"_result_"$vm_exhaustive"_"$numa_exhaustive".xml" $DIR_RESULT"/"$test"_result_"$vm_exhaustive"_"$numa_exhaustive".huawei" $NEW_CONFIG_FILE  $DIR_RESULT"/"$test"_result_"$vm_exhaustive"_"$numa_exhaustive".txt"
            $ALGO_PATH $DIR_TEST"/"$test".dcxml" $DIR_RESULT"/"$test"_result_"$vm_exhaustive"_"$numa_exhaustive".xml" $DIR_RESULT"/"$test"_result_"$vm_exhaustive"_"$numa_exhaustive".huawei" $NEW_CONFIG_FILE > $DIR_RESULT"/"$test"_result_"$vm_exhaustive"_"$numa_exhaustive".txt" &
            pids[${i}]=$!
            let "i+=1"
        done
    done

    # waiting until algos will be finished
    echo "waiting"
    for pid in ${pids[*]}
    do
        wait $pid
    done
done
