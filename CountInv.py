import pytest


def count_inversions(x):
    """
    Function counts the number of inversions, which is a pair of elements that are out of order, in an array x.
    INPUT: x array
    OUTPUT: Number of inversions in x integer
    """
    count = 0
    n = len(x)

    # base case
    if n <= 1:
        return 0
    else:
        x_left = x[range(0, n/2)]
        x_right = x[range(n/2, n)]

        split_inversions = count_inversions(x)

    return count