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
    # print(f'jobs {jobs}')
    # loop = 0
    r = []
    ld = defaultdict(list)
    for j in jobs:
        ld[j] = []
    for d in deps:
        ld[d[1]].append(d[0])

    # print(f'ld {ld}')
    while len(jobs):
        # loop += 1
        # if loop >= 10:
        #     print(f'jobs {jobs}')
        #     break
        empty_keys = [k for k in ld.keys() if len(ld[k]) == 0]
        # print(f"empty_keys {empty_keys}")
        if len(empty_keys) == 0:
            return []
        for k in empty_keys:
            if k in jobs:
                jobs.remove(k)
                r.append(k)
            del ld[k]

            for i, (key, value) in enumerate(ld.items()):
                if k in value:
                    ld[key].remove(k)
    # print(f'returning _______________{r}________')
    return r


if __name__ == "__main__":
    tasksx = [1, 2, 3, 4, 5, 6, 7, 8]
    depsx = [[4, 2], [1, 2], [1, 8], [6, 8], [6, 3], [2, 5], [7, 8], [2, 3], [8, 7]]
    print("topological_sort", topological_sort(tasksx, depsx))
