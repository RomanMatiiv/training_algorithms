"""
https://contest.yandex.ru/contest/27393/problems/A/
"""


def freeze_mode(temp_source: int, temp_dest: int) -> int:
    pass


def heat_mode(temp_source: int, temp_dest: int) -> int:
    pass


def auto_mode(temp_source: int, temp_dest: int) -> int:
    if temp_source > temp_dest:
        return freeze_mode(temp_source, temp_dest)

    if temp_source < temp_dest:
        return heat_mode(temp_source, temp_dest)

    else:
        return temp_source


def fan_mode(temp_source: int, temp_dest) -> int:
    return temp_source


SELECTOR = {"freeze": freeze_mode}


if __name__ == "__main__":
    temp_raw = input().split()
    temp_source = int(temp_raw[0])
    temp_dest = int(temp_raw[0])

    work_mode_raw = input().strip().lower()

    work_mode = SELECTOR[work_mode_raw]

    feature_temp = work_mode(temp_source, temp_dest)

    print(feature_temp)