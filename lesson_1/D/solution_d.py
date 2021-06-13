"""
https://contest.yandex.ru/contest/27393/problems/D/
"""


class NoSolution(Exception):
    pass


class ManySolution(Exception):
    pass


def get_solution(a: int, b: int, c: int) -> int:

    if c < 0:
        raise NoSolution

    elif a == 0 and b == c*c:
        raise ManySolution

    elif a == 0:
        raise NoSolution

    x = (c*c - b)/a

    if int(x) == x:
        return int(x)
    else:
        raise NoSolution


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    try:
        x = get_solution(a=a, b=b, c=c)
    except NoSolution:
        print("NO SOLUTION")
    except ManySolution:
        print("MANY SOLUTIONS")
    else:
        print(x)