import pytest
from topological_sort import *


def test_valid_one():
    tasks = [4, 3, 2, 1]
    deps = [
        [2, 3],
        [2, 4],
        [4, 3],
        [1, 3],
        [1, 4],
    ]
    ordered = topological_sort(tasks, deps)
    assert is_topol_ordered(ordered, tasks, deps) == True


def test_valid_two():
    tasks = [1, 2, 3, 4, 5]
    deps = [[1, 3], [2, 3], [3, 4], [2, 5], [5, 4]]
    ordered = topological_sort(tasks, deps)
    assert is_topol_ordered(ordered, tasks, deps) == True


def test_valid_three():
    tasks = [1, 2, 3, 4, 5, 6, 7, 8]
    deps = [[3, 1], [8, 1], [8, 7], [5, 7], [
        5, 2], [1, 4], [1, 6], [1, 2], [7, 6]]
    ordered = topological_sort(tasks, deps)
    assert is_topol_ordered(ordered, tasks, deps) == True


def test_invalid():
    tasks = [1, 2, 3, 4, 5, 6, 7, 8]
    deps = [[4, 2], [1, 2], [1, 8], [6, 8], [
        6, 3], [2, 5], [7, 8], [2, 3], [8, 7]]
    # No valid order
    assert len(topological_sort(tasks, deps)) == 0


def is_topol_ordered(ordered, tasks, deps):
    deps_graph = {}
    if len(ordered) != len(tasks):
        return False
    oSet = set()
    tSet = set()
    for i in range(len(tasks)):
        oSet.add(ordered[i])
        tSet.add(tasks[i])

    if len(oSet.difference(tSet)) != 0:
        return False

    for d in deps:
        if d[1] in deps_graph:
            deps_graph[d[1]].append(d[0])
        else:
            deps_graph[d[1]] = [d[0]]

    for t in ordered:
        if t in deps_graph and len(deps_graph[t]):
            return False
        for d in deps_graph.values():
            if t in d:
                d.remove(t)
    return True
