from solution import freeze_mode
from solution import heat_mode
from solution import auto_mode
from solution import fan_mode


def test_fan_mode():
    t_room = 10

    want_temp = t_room

    assert want_temp == fan_mode(t_room, None)

    assert want_temp == fan_mode(temp_source, None)