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
        raise NotImplemented

    def __lt__(self, other):
        raise NotImplemented

    def __gt__(self, other):
        raise NotImplemented


def get_all_rectangle(brick: Brick) -> List[Rectangle]:
    raise NotImplemented


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

