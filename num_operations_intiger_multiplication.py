"""
PROBLEM: Integer Multiplication
How many operations are necessary to solve the following?
    Input: Two n-digit nonnegative integers, x and y
    Output: The product x*y
"""


def grade_school_method(x, y):
    """multiply x and y by summing up partial products of x and y"""
    operation_counter = 0

    n = len(str(x))
    res = list(range(n))
    x_str = str(x)
    x_array = [x_str[j] for j in range(n)]
    y_array = [str(y)[j] for j in range(n)]

    for op_0 in range(n):
        operation_counter += 1
        res[op_0] = (int(x_array[op_0]) * pow(10, op_0 + 1)) * y

        res_c = int(x_array[op_0]) * int(y_array[op_0])
        if res_c > 9:
            operation_counter += 1

    for op_1 in range(n):




def test_grade_school_method(x, y):
    x = 1234
    y = 5678


