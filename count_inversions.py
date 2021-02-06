import pytest
import numpy as np


def count_inversions(x):
    """
    Function counts the number of inversions, which is a pair of elements that are out of order, in an array x.
    INPUT: x list
    OUTPUT: Number of inversions in x integer
    """

    n = len(x)

    if n == 1:
        # base case
        return x, 0
    else:
        x_left = x[:n // 2]
        x_right = x[n // 2:]

        x_left, x_left_i = count_inversions(x_left)
        x_right, x_right_i = count_inversions(x_right)
        c = []

        i = 0
        j = 0
        inversions = 0 + x_left_i + x_right_i

        while i < len(x_left) and j < len(x_right):
            if x_left[i] < x_right[j]:
                c.append(x_left[i])
                i += 1
            else:
                c.append(x_right[j])
                j += 1
                inversions += (len(x_left) - i)

        c += x_left[i:]
        c += x_right[j:]

    return c, inversions


def test_small_array(x=[0, 1, 2, 3]):
    out_array, inversions = count_inversions(x)
    assert inversions == 0


def test_odd_len_array(x=[0, 7, 2, 3]):
    out_array, inversions = count_inversions(x)
    assert inversions == 2


