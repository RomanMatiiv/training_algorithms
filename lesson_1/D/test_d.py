import pytest

from solution_d import get_solution
from solution_d import NoSolution
from solution_d import ManySolution


def test_one_solution_case_1():
    a = 1
    b = 2
    c = 3

    true_x = 7

    x = get_solution(a=a, b=b, c=c)

    assert x == true_x


def test_one_solution_case_2():
    a = 1
    b = 0
    c = 0

    true_x = 0

    x = get_solution(a=a, b=b, c=c)

    assert x == true_x


def test_many_solution():
    a = 0
    b = 4
    c = 2

    with pytest.raises(ManySolution):
        get_solution(a=a, b=b, c=c)


def test_no_solution():
    a = 1
    b = 2
    c = -3

    with pytest.raises(NoSolution):
        get_solution(a=a, b=b, c=c)


def test_float_solution():
    a = 4
    b = 2
    c = 3

    true_x = 1.75

    with pytest.raises(NoSolution):
        get_solution(a=a, b=b, c=c)