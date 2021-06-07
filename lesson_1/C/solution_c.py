import re


def extract_telephone_number(tel_number: str) -> int:
    tel_number = tel_number.replace("+7", "8")

    tel_number = re.findall('\d+', tel_number)
    tel_number = "".join(tel_number)
    if len(tel_number) != 11:
        tel_number = tel_number[0] + "495" + tel_number[1:]

    return int(tel_number)


if __name__ == "__main__":
    tel_number_add = input()
    for _ in range(3):
        cur_tel_number = input()
