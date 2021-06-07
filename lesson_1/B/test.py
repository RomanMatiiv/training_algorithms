from solution_b import triangle_exist


def test_from_example_1():
    a = 3
    b = 4
    c = 5

    assert triangle_exist(a, b, c) is True


def test_from_example_2():
    a = 4
    b = 5
    c = 4

    assert triangle_exist(a, b, c) is True


def test_from_example_3():
    a = 4
    b = 5
    c = 3

    assert triangle_exist(a, b, c) is True


def test_from_example_more():
    a = 9
    b = 2
    c = 6

    assert triangle_exist(a, b, c) is False


def test_from_example_equal():
    a = 8
    b = 2
    c = 6

    assert triangle_exist(a, b, c) is False


