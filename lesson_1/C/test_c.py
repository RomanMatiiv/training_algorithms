from solution_c import extract_telephone_number


def test_case_1():
    expect_tel_number = 4954302397

    real_tel_num = extract_telephone_number("+7-4-9-5-43-023-97")

    assert real_tel_num == expect_tel_number


def test_case_2():
    expect_tel_number = 4954302397

    real_tel_num = extract_telephone_number("8(495)430-23-97")

    assert real_tel_num == expect_tel_number


def test_case_3():
    expect_tel_number = 4954302397

    real_tel_num = extract_telephone_number("8(495)430-23-97")

    assert real_tel_num == expect_tel_number


def test_case_4():
    expect_tel_number = 4954302397

    real_tel_num = extract_telephone_number("4-3-0-2-3-9-7")

    assert real_tel_num == expect_tel_number


