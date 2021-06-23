import pytest

from solution_i import Rectangle
from solution_i import Brick
from solution_i import get_all_rectangle


def test_rectangle_init():
    Rectangle(width=10, height=5)


def test_rectangle_equals():
    rect_1 = Rectangle(width=10, height=5)
    rect_2 = Rectangle(width=10, height=5)
    rect_3 = Rectangle(width=5, height=10)

    assert rect_1 == rect_2
    assert rect_1 == rect_3
    assert rect_2 == rect_3

    assert rect_2 == rect_1
    assert rect_3 == rect_1
    assert rect_3 == rect_2


def test_rectangle_not_equal():
    rect_1 = Rectangle(width=5, height=10)
    rect_2 = Rectangle(width=4, height=7)
    assert rect_1 != rect_2

    rect_1 = Rectangle(width=4, height=10)
    rect_2 = Rectangle(width=5, height=8)
    assert rect_1 != rect_2


def test_rectangle_greater():
    rect_greater = Rectangle(width=5, height=10)
    rect_less = Rectangle(width=4, height=9)
    assert rect_greater > rect_less

    rect_greater = Rectangle(width=5, height=10)
    rect_less = Rectangle(width=4, height=10)
    assert rect_greater > rect_less

    rect_greater = Rectangle(width=10, height=5)
    rect_less = Rectangle(width=4, height=10)
    assert rect_greater > rect_less

    rect_greater = Rectangle(width=5, height=10)
    rect_less = Rectangle(width=5, height=9)
    assert rect_greater > rect_less


def test_get_all_rectangle():
    brick = Brick(width=10, height=5, length=3)

    rect_1 = Rectangle(width=10, height=5)
    rect_2 = Rectangle(width=10, height=3)
    rect_3 = Rectangle(width=5, height=3)

    all_possible_rectangle = [rect_1,
                              rect_2,
                              rect_3]

    for cur_rec in get_all_rectangle(brick):
        assert cur_rec in all_possible_rectangle
