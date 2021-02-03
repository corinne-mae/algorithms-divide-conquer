import pytest


def merge_sort(x):

    if len(x) > 1:
        # find midpoint of array
        mid = len(x) // 2

        # split x into 2 new arrays
        left_array = x[:mid]
        right_array = x[mid:]

        # recursively call merge_sort
        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0
        # loop through both left and right arrays
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                x[k] = left_array[i]
                i += 1
            else:
                x[k] = right_array[j]
                j += 1
            k += 1
        # when all elements in right_array have been copied over
        while i < len(left_array):
            x[k] = left_array[i]
            i += 1
            k += 1
        # when all elements in left_array have been copied over
        while j < len(right_array):
            x[k] = right_array[j]
            j += 1
            k += 1

    return x


def test_merge_sort():
    a = [3, 8, 2, 1]
    a_ans = [1, 2, 3, 8]
    a_qs = merge_sort(a)
    assert a_qs == a_ans


def test_odd_length_merge_sort():
    a = [3, 8, 2, 1, 5]
    a_ans = [1, 2, 3, 5, 8]
    a_qs = merge_sort(a)
    assert a_qs == a_ans


