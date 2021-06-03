from solution import freeze_mode
from solution import heat_mode
from solution import auto_mode
from solution import fan_mode


def test_fan_mode():
    temp_source = 10

    want_temp = temp_source

    assert want_temp == fan_mode(temp_source, None)