"""
https://contest.yandex.ru/contest/27393/problems/B/
"""

def triangle_exist(a: int, b: int, c: int) -> bool:
    if (a + b) <= c:
        return False
    if (a + c) <= b:
        return False
    if (b + c) <= a:
        return False
    else:
        return True


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    if triangle_exist(a, b, c):
        print("YES")
    else:
        print("NO")
