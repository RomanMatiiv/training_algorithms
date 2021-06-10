import re


def extract_telephone_number(raw_tel_number: str) -> int:
    raw_tel_number = raw_tel_number.replace("+7", "8")

    raw_tel_number = re.findall('\d+', raw_tel_number)
    raw_tel_number = "".join(raw_tel_number)

    _tel_number = None
    _tel_code = None

    # номер телефона
    _tel_number = raw_tel_number[-7:]

    # код города
    if len(raw_tel_number) == 11:  # все числа есть
        _tel_code = raw_tel_number[1:4]
    elif len(raw_tel_number) == 10:  # нет 8
        _tel_code = raw_tel_number[:3]
    elif len(raw_tel_number) == 8 or len(raw_tel_number) == 7:  # нет кода города
        _tel_code = "495"

    tel_number = _tel_code + _tel_number
    tel_number = int(tel_number)

    return int(tel_number)


if __name__ == "__main__":
    tel_number_add = input()

    tel_number_add = extract_telephone_number(tel_number_add)

    for _ in range(3):
        cur_tel_number = input()
        cur_tel_number = extract_telephone_number(cur_tel_number)
        if tel_number_add == cur_tel_number:
            print("YES")
        else:
            print("NO")
