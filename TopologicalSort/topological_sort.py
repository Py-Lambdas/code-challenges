# """
# Topological Sort
# Difficulty: Hard
# Given a list of tasks and a list of dependencies return
# a list of tasks in valid order. If no such order exists
# return an empty array.
#
# tasks = [1,2,3,4]
# deps = [
#     [2, 3],
#     [2, 4],
#     [4, 3],
#     [1, 3],
#     [1, 4],
# ]
#
# topological_sort(tasks, deps) = [1,2,4,3] or [2,1,4,3]
#
# Author: BrannanC
# """
from collections import defaultdict


def topological_sort(j, deps):
    jobs = j[::1]
    r = []
    ld = defaultdict(list)
    lj = defaultdict(list)
    for j in jobs:
        ld[j] = []
    for d in deps:
        ld[d[1]].append(d[0])
        lj[d[0]].append(d[1])
    while len(jobs):
        empty_keys = [k for k in ld.keys() if len(ld[k]) == 0]
        if len(empty_keys) == 0:
            return []
        for k in empty_keys:
            if k in jobs:
                jobs.remove(k)
                r.append(k)
            del ld[k]
            for d in lj[k]:
                ld[d].remove(k)
    return r


if __name__ == "__main__":
    tasksx = [4, 3, 2, 1]
    depsx = [
        [2, 3],
        [2, 4],
        [4, 3],
        [1, 3],
        [1, 4],
    ]
    print("topological_sort", topological_sort(tasksx, depsx))
