"""
Topological Sort
Difficulty: Hard
Given a list of tasks and a list of dependencies return
a list of tasks in valid order. If no such order exists
return an empty array.

tasks = [1,2,3,4]
deps = [
    [2, 3],
    [2, 4],
    [4, 3],
    [1, 3],
    [1, 4],
]

topological_sort(tasks, deps) = [1,2,3,4] or [2,1,3,4]

Author: BrannanC
"""
from collections import defaultdict

def topological_sort(jobs, deps):
    r = []
    ld = defaultdict(list)
    for d in deps:
        ld[d[1]].append(d[0])
    while len(jobs):
        empty_keys = [k for k in ld.keys() if len(ld[k]) == 0]
        if len(empty_keys) == 0:
            return []
        for k in empty_keys:
            jobs.remove(k)
            r.append(k)
            for k, value in ld:
                if value == k:
                    ld[value].remove(k)
    return r
