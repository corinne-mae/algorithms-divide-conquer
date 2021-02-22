"""
Programming assignment 3:

Count the number of comparisons in the Quick Sort algorithm using 3 different methods for choosing the pivot:
  1) First element in array
  2) last element in array
  3) "Median of 3" rule, which is the median of the first, middle, and final element in the array
"""

import numpy as np
import pytest

comparisons = 0

PIVOT_FIRST = 1
PIVOT_LAST = 2
PIVOT_MEDIAN = 3


def swap(a: np.ndarray, i: int, j: int):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp


def is_median(x, i, j, k):
    return (x[j] > x[i] > x[k]) or (x[j] < x[i] < x[k])


def _quick_sort(x: np.ndarray, l: int, r: int, pivot_method):
    global comparisons

    # Base case
    if l >= r:
        return x

    p = 0
    if pivot_method == PIVOT_FIRST:
        p = x[l]

    elif pivot_method == PIVOT_LAST:
        p = x[r]
        swap(x, l, r)

    elif pivot_method == PIVOT_MEDIAN:
        m = l + ((r - l) >> 1)
        if is_median(x, l, m, r):
            p = x[l]
        elif is_median(x, m, l, r):
            p = x[m]
            swap(x, l, m)
        else:
            p = x[r]
            swap(x, l, r)

    # update comparisons
    comparisons += (r - l)

    # Partition
    i = l + 1
    for j in range(l + 1, r + 1):
        if x[j] < p:
            swap(x, i, j)
            i += 1
    swap(x, l, i - 1)

    # Recursive Calls
    _quick_sort(x, l, i - 2, pivot_method)
    _quick_sort(x, i, r, pivot_method)

    return x, comparisons


def quick_sort(x, pivot_method):
    right = len(x) - 1
    output_x, output_comparisons = _quick_sort(x, 0, right, pivot_method)
    return output_x, output_comparisons


def test_quick_sort():
    a = np.array([3, 8, 2, 5, 1])
    a_ans = np.array([1, 2, 3, 5, 8])
    a_qs, cnts = quick_sort(a, PIVOT_FIRST)

    assert all(a_ans == a_qs)


def read_assignment_array():
    assignment_array = []
    file_path = '../assignments/QuickSort.txt'
    with open(file_path) as fp:
        for line in fp.readlines():
            assignment_array.append(int(line))
    return assignment_array


def test_problem_one():
    assignment_array = read_assignment_array()
    input_array = assignment_array[:]  # make a copy
    output, out_comparisons = quick_sort(input_array, PIVOT_FIRST)
    print(out_comparisons)


def test_problem_two():
    assignment_array = read_assignment_array()
    input_array = assignment_array[:]  # make a copy
    output, out_comparisons = quick_sort(input_array, PIVOT_LAST)
    print(out_comparisons)


def test_problem_three():
    assignment_array = read_assignment_array()
    input_array = assignment_array[:]  # make a copy
    output, out_comparisons = quick_sort(input_array, PIVOT_MEDIAN)
    print(out_comparisons)