import pytest


def rec_int_mult(x, y):
    """multiply x and y by summing up partial products of x and y"""

    def get_sign(x, y):
        if x < 0 and y < 0:
            sign = 1
        if x > 0 and y > 0:
            sign = 1
        else:
            sign = -1
        return sign

    sign = get_sign(x, y)
    x_a = abs(x)
    y_a = abs(y)

    if len(str(x_a)) == 0 or len(str(y_a)) == 0:
        return 1

    if len(str(int(x_a))) == 1 or len(str(int(y_a))) == 1:
        return x * y

    else:
        n = max(len(str(x_a)), len(str(y_a)))
        half_n = int(n // 2)

        a = x_a // pow(10, half_n)
        b = x_a % pow(10, half_n)

        c = y_a // pow(10, half_n)
        d = y_a % pow(10, half_n)

        ac = rec_int_mult(a, c)
        ad = rec_int_mult(a, d)
        bc = rec_int_mult(b, c)
        bd = rec_int_mult(b, d)

        out = (pow(10, n))*ac + (pow(10, half_n))*(ad + bc) + bd
        return sign * out


def test_multiplication_1(x=1, y=1):
    assert rec_int_mult(x, y) == 1


def test_multiplication_ten(x=10, y=10):
    assert rec_int_mult(x, y) == 100


def test_multiplication_two_digits(x=22, y=55):
    assert rec_int_mult(x, y) == 1210


def test_multiplication_incorrect(x=22, y=55):
    assert rec_int_mult(x, y) != 121


def test_multiplication_large_numbers(
        x=3141592653589793238462643383279502884197169399375105820974944592,
        y=2718281828459045235360287471352662497757247093699959574966967627):
    assert rec_int_mult(x, y) == 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184


def test_negative_multiplication(x=-22, y=55):
    assert rec_int_mult(x, y) == -1210

