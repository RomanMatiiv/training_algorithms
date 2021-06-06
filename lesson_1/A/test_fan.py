from solution import fan_mode


def test_fan_mode_equal_1():
    t_room = -10
    t_cond = -10

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp


def test_fan_mode_equal_2():
    t_room = 0
    t_cond = 0

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp


def test_fan_mode_equal_3():
    t_room = 10
    t_cond = 10

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp


def test_fan_mode_above_1():
    t_room = -10
    t_cond = 0

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp


def test_fan_mode_above_2():
    t_room = -10
    t_cond = 10

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp


def test_fan_mode_above_3():
    t_room = 0
    t_cond = 10

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp


def test_fan_mode_less_1():
    t_room = 0
    t_cond = -10

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp


def test_fan_mode_less_2():
    t_room = 10
    t_cond = -10

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp


def test_fan_mode_less_3():
    t_room = 20
    t_cond = 10

    want_temp = t_room

    assert fan_mode(t_room, t_cond) == want_temp