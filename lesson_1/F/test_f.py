from solution_f import get_minimal_table
from solution_f import RectangleObject


def test_case_1():
    obj_1 = RectangleObject(width=10, height=2)
    obj_2 = RectangleObject(width=2, height=10)

    final_obj = get_minimal_table(obj_1, obj_2)

    assert (final_obj.width == 20 and final_obj.height == 2 or
            final_obj.height == 20 and final_obj.width == 2 or
            final_obj.width == 10 and final_obj.height == 4 or
            final_obj.height ==10 and final_obj.width == 4)


def test_case_2():
    obj_1 = RectangleObject(width=5, height=7)
    obj_2 = RectangleObject(width=3, height=2)

    final_obj = get_minimal_table(obj_1, obj_2)

    assert (final_obj.width == 9 and final_obj.height == 5 or
            final_obj.height == 5 and final_obj.width == 9)
