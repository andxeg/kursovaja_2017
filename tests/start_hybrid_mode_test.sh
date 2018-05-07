#!/bin/bash

# LAUNCH ALGO IN HYBRID MODE
# WITHOUT LIMITING THE GENERALITY TEST ONLY NUMA CONSTRAINT

ALGO_PATH=$1
CONFIG_FILE=$2
DIR_TEST=$3
DIR_RESULT=$4

NUMA_CONSTRAINT_MIN=0.1
NUMA_CONSTRAINT_MAX=0.6
NUMA_CONSTRAINT_STEP=0.1

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
    for numa_constraint in $(seq $NUMA_CONSTRAINT_MIN $NUMA_CONSTRAINT_STEP $NUMA_CONSTRAINT_MAX)
    do
        NEW_CONFIG_FILE=$CONFIG_FILE"_"$test"_"$numa_constraint
        cp $CONFIG_FILE $NEW_CONFIG_FILE
        sed -i "s/^\(numa_constraint\s*=\s*\).*\$/\1$numa_constraint/" $NEW_CONFIG_FILE
        echo $ALGO_PATH $DIR_TEST"/"$test".dcxml" $DIR_RESULT"/"$test"_result_"$numa_constraint".xml" $DIR_RESULT"/"$test"_result_"$numa_constraint".huawei" $NEW_CONFIG_FILE  $DIR_RESULT"/"$test"_result_"$numa_constraint".txt"
        $ALGO_PATH $DIR_TEST"/"$test".dcxml" $DIR_RESULT"/"$test"_result_"$numa_constraint".xml" $DIR_RESULT"/"$test"_result_"$numa_constraint".huawei" $NEW_CONFIG_FILE > $DIR_RESULT"/"$test"_result_"$numa_constraint".txt" &
        pids[${i}]=$!
        let "i+=1"
    done

    # waiting until algos will be finished
    echo "waiting"
    for pid in ${pids[*]}
    do
        wait $pid
    done
done
