import numpy as np
import pytest


def swap(a: np.ndarray, i: int, j: int):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp
    return a


def quick_sort(x: np.ndarray, l: int, r: int):

    if l >= r:
        return x

    def partition(a_p: np.ndarray, l_p: int, r_p: int):
        p = a_p[l_p]
        # boundary between items with values less than the pivot value and those greater than the pivot value
        i_p = l_p + 1
        # j is boundary between partitioned items in the array and un-partitioned values
        for j in range(l_p + 1, r_p + 1):
            if a_p[j] < p:
                # swap a[i] and a[j]
                tmp = a_p[j]
                a_p[j] = a_p[i_p]
                a_p[i_p] = tmp
                i_p += 1

        # swap a[l] and a[i - 1]
        tmp = a_p[l_p]
        a_p[l_p] = a_p[i_p - 1]
        a_p[i_p - 1] = tmp

        return i_p - 1

    # 1. i = choose pivot(x, l, r)
    i = int(np.random.randint(l, r, 1))
    x = swap(x, l, i)
    j = partition(x, l, r)
    quick_sort(x, l, j-1)
    quick_sort(x, j+1, r)

    return x


def test_quick_sort():
    a = np.array([3, 8, 2, 5, 1])
    a_ans = np.array([1, 2, 3, 5, 8])
    a_qs = quick_sort(a, 0, 4)
    assert all(a_ans == a_qs)


