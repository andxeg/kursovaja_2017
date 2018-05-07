#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt


TEST_NAME_NUMBER_MAP = {
    "0": "vm_not_exh + numa_not_exh",
    "1": "vm_not_exh + numa_exh",
    "2": "vm_exh + numa_not_exh",
    "3": "vm_exh + numa_exh"
}

def result_from_file(filename):
    result = None
    file = open(filename, "r")
    line = file.readline()
    total_requests = 1
    assigned_requests = 0
    while line != "":
        if "Requests all" in line:
            total_requests = int(line.split('->')[-1])
        
        if "Requests assigned" in line:
            assigned_requests = int(line.split('->')[-1])

        line = file.readline()

    file.close()
    result = float(assigned_requests) / total_requests
    return result

def collect_results(directory_name):
    result = {}
    files = [f for f in os.listdir(directory_name) 
            if os.path.isfile(os.path.join(directory_name, f))
            and "txt" in f]

    for file in files:
        l = file.split('_')
        test_name = '_'.join(l[:3])
        test_number = int(''.join(l[4] + l[5].split('.')[0]), 2)
        if test_name not in result:
            result[test_name] = {}

        res = result_from_file(os.path.join(directory_name, file))
        result[test_name].update({str(test_number): res})

    return result

def draw_diagrams(data):
    items = sorted(data.items(), key=lambda x: x[0])
    bar_width = 0.2
    bars1 = [test_result[1]["0"] for test_result in items]
    bars2 = [test_result[1]["1"] for test_result in items]
    bars3 = [test_result[1]["2"] for test_result in items]
    bars4 = [test_result[1]["3"] for test_result in items]
    
    # the x position of bars
    r1 = np.arange(len(bars1))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]

    # create "vm_not_exh + numa_not_exh" bars
    plt.bar(r1, bars1, width=bar_width, color = 'blue', edgecolor='black', capsize=7, label=u'Запрещена миграция виртуальных машин между серверами и NUMA блоками')

    # create "vm_not_exh + numa_exh" bars
    plt.bar(r2, bars2, width=bar_width, color = 'cyan', edgecolor='black', capsize=7, label=u'Запрещена миграция виртуальных машин между серверами, разрешена между NUMA блоками')

    # create "vm_exh + numa_not_exh" bars
    plt.bar(r3, bars3, width=bar_width, color = 'red', edgecolor='black', capsize=7, label=u'Разрешена миграция виртуальных машин между серверами, запрещена миграция между NUMA блоками')

    # create "vm_exh + numa_exh" bars
    plt.bar(r4, bars4, width=bar_width, color = 'yellow', edgecolor='black', capsize=7, label=u'Разрешена миграция виртуальных машин между серверами и NUMA-блоками')

    # general layout
    # plt.xticks([r + bar_width for r in range(len(bars1))], [item[0] for item in items])
    plt.xticks([r + bar_width for r in range(len(bars1))], range(1,17))
    plt.xlabel(u"Номер теста")
    plt.ylabel(u"Доля размещенных запросов")
    plt.legend()

    plt.show()

# python collect_results_migration_test.py ./output/migration/
if __name__=="__main__":
    if len(sys.argv) != 2:
        print("error in input parameters")
        print("type %s <directory_with_result_migration_test>" % sys.argv[0])
        exit()

    directory_name = sys.argv[1]
    result = collect_results(directory_name)
    print(len(result))
    print(json.dumps(result, sort_keys=True, indent=4))
    draw_diagrams(result)
