"""
https://contest.yandex.ru/contest/27393/problems/A/
"""


def freeze_mode(t_room: int, t_cond: int) -> int:
    if t_cond >= t_room:
        return t_room
    else:
        return t_cond


def heat_mode(t_room: int, t_cond: int) -> int:
    if t_cond >= t_room:
        return t_cond
    else:
        return t_room


def auto_mode(t_room: int, t_cond: int) -> int:
    if t_room > t_cond:
        return freeze_mode(t_room, t_cond)

    if t_room < t_cond:
        return heat_mode(t_room, t_cond)

    else:
        return t_room


def fan_mode(t_room: int, t_cond) -> int:
    return t_room


SELECTOR = {"freeze": freeze_mode}


if __name__ == "__main__":
    temp_raw = input().split()
    t_room = int(temp_raw[0])
    t_cond = int(temp_raw[1])

    work_mode_raw = input().strip().lower()

    work_mode = SELECTOR[work_mode_raw]

    feature_temp = work_mode(t_room, t_cond)

    print(feature_temp)