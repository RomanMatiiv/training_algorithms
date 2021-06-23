from dataclasses import dataclass
from typing import List


@dataclass
class Brick:
    width: int
    height: int
    length: int


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if ((self.width == other.width and self.height == other.height) or
            (self.height == other.width and self.width == other.height)):
            return True
        else:
            return False

    def __lt__(self, other):
        # TODO обработать случай когда стороны поменяли местами
        if ((self.width == other.width and self.height < other.height) or
            (self.height == other.height and self.width < other.width) or
            (self.width < other.width and self.height < other.height)):
            return True
        else:
            return False


def get_all_rectangle(brick: Brick) -> List[Rectangle]:
    rect_1 = Rectangle(width=brick.width, height=brick.height)
    rect_2 = Rectangle(width=brick.width, height=brick.length)
    rect_3 = Rectangle(width=brick.height, height=brick.length)

    return [rect_1, rect_2, rect_3]


if __name__ == "__main__":
    A, B, C, D, E = [int(i) for i in input().split()]

    brick = Brick(A, B, C)
    hole = Rectangle(D, E)

    res = False
    for cur_rec in get_all_rectangle(brick):
        if cur_rec <= hole:
            res = True

    if res:
        print("YES")
    else:
        print("NO")

