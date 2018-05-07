#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

def result_from_file(filename):
    result = {
        "assigned_requests": 0,
        "performance": {
            "VCPUs": {
                "LOW": 0,
                "HIGH": 0
            },
            "RAM": {
                "LOW": 0,
                "HIGH": 0
            }
        },
        "performance_index": 0
    }

    file = open(filename, "r")
    line = file.readline()
    total_requests = 1
    assigned_requests = 0
    while line != "":
        if "Requests all" in line:
            total_requests = int(line.split('->')[-1])
        
        if "Requests assigned" in line:
            assigned_requests = int(line.split('->')[-1])

        l = line.split()
        if ("VCPUs" in line or "RAM" in line) and len(l) == 1:
            line = file.readline()
            line = file.readline()
            high = int(line.split(':')[-1])
            result["performance"][l[0]]["HIGH"] = high
            line = file.readline()
            low = int(line.split(':')[-1])
            result["performance"][l[0]]["LOW"] = low

            result["performance_index"] = 1 if (low + high) == 0 else float(low) / (low + high)

        line = file.readline()

    file.close()
    result["assigned_requests"] = float(assigned_requests) / total_requests
    return result

def collect_results(directory_name):
    result = {}
    files = [f for f in os.listdir(directory_name) 
            if os.path.isfile(os.path.join(directory_name, f))
            and "txt" in f]

    for file in files:
        l = file.split('_')
        test_name = '_'.join(l[:3])
        numa_constraint = float(l[4].split('.')[1]) / 10
        if test_name not in result:
            result[test_name] = {}
            result[test_name].update({"numa_constraint":[]})
            result[test_name].update({"assigned_requests":[]})
            result[test_name].update({"performance":[]})

        res = result_from_file(os.path.join(directory_name, file))
        result[test_name]["numa_constraint"]\
                        .append(numa_constraint)
        result[test_name]["assigned_requests"]\
                        .append(res["assigned_requests"])
        result[test_name]["performance"]\
                        .append(res["performance_index"])

    return result

def draw_diagrams(data):
    nrows = 3
    ncols = 5
    nrows, ncols = ncols, nrows
    fig, axes = plt.subplots(nrows,ncols)
    fig.suptitle(u"Результаты исследования гибридного подхода", fontsize=20)

    items = sorted(data.items(), key=lambda x: x[0])
    for name, result in items:
        test_group = int(name.split('_')[0][1])
        numa = int(name.split('_')[-1])
        
        performance = zip(result["numa_constraint"], result["performance"])
        performance = sorted(performance, key=lambda x: x[0])
        x, y1 = zip(*performance)
        # y1 = map(lambda t: round(t, 4), y1)

        assigned_requests = zip(result["numa_constraint"], result["assigned_requests"])
        assigned_requests = sorted(assigned_requests, key=lambda x: x[0])
        x, y2 = zip(*assigned_requests)
        # y2 = map(lambda t: round(t, 4), y2)

        color = "tab:red"
        row = numa / 2
        col = test_group - 1
        row, col = col, row
        linestyle = '-'
        if row == 0:
            axes[row, col].set_xlabel(u"NUMA порог")
            axes[row, col].set_title(u"Тесты 1-5, NUMA=%s" % str(numa))
        if row == 2:
            axes[row, col].set_ylabel(u"Индекс производительности", color=color, fontsize=20)
        axes[row, col].plot(x, y1, linestyle=linestyle, color=color)
        axes[row, col].tick_params(axis='y', labelcolor=color)
        axes[row, col].grid(True)

        ax2 = axes[row, col].twinx()

        color = "tab:blue"
        if row == 2:            
            ax2.set_ylabel(u"Доля размещенных запросов", color=color, fontsize=20)
        ax2.plot(x, y2, linestyle=linestyle, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()    
    # Format the minor tick labels of the y-axis into empty strings with
    # `NullFormatter`, to avoid cumbering the axis with too many labels.
    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    # Adjust the subplot layout, because the logit one may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.05, right=0.95, hspace=0.45,
                        wspace=0.60)

    # fig.savefig("numa_constraint")
    plt.show()

# python collect_results_hybrid_mode_test.py ./output/hybrid_mode/ | less
if __name__=="__main__":
    if len(sys.argv) != 2:
        print("error in input parameters")
        print("type %s <directory_with_results_hybrid_test>" % sys.argv[0])
        exit()

    directory_name = sys.argv[1]
    result = collect_results(directory_name)
    print(len(result))
    print(json.dumps(result, sort_keys=True, indent=4))
    draw_diagrams(result)
