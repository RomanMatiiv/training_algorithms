"""
https://contest.yandex.ru/contest/27393/problems/F/
"""


class RectangleObject:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.square = width * height

    def __eq__(self, other):
        if self.square == other.square:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.square < other.square:
            return True
        else:
            return False


def get_minimal_table(obj_1: RectangleObject, obj_2: RectangleObject) -> RectangleObject:

        table_1 = RectangleObject(width=obj_1.height+obj_2.width,
                                  height=max(obj_1.width, obj_2.height))
        table_2 = RectangleObject(width=obj_1.width+obj_2.height,
                                  height=max(obj_1.height, obj_2.width))
        table_3 = RectangleObject(width=obj_1.height+obj_2.height,
                                  height=max(obj_1.width, obj_2.width))
        table_4 = RectangleObject(width=obj_1.width+obj_2.width,
                                  height=max(obj_1.height, obj_2.height))

        min_table = min([table_1, table_2, table_3, table_4])

        return min_table


if __name__ == "__main__":

    w1, h1, w2, h2 = [int(i) for i in input().split()]

    notebook_1 = RectangleObject(width=w1, height=h1)
    notebook_2 = RectangleObject(width=w2, height=h2)

    min_table = get_minimal_table(notebook_1, notebook_2)

    print(min_table.width, min_table.height)