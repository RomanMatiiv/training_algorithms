"""
https://contest.yandex.ru/contest/27393/problems/D/
"""


def get_solution(a: int, b: int, c: int):
    x = None

    if a == 0 and b == c*c:
        print("MANY SOLUTION")
        return x

    elif a == 0:
        print("NO SOLUTION")
        return x

    x = (c*c - b)/a

    if int(x) == x:
        return x
    else:
        print("NO SOLUTION")
        return None



if __name__ == "__main__":
    pass