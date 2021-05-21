from datetime import datetime
import fire


YEAR = 2000
ZODIAC_SIGNS = {
    (datetime(YEAR, 1, 20), datetime(YEAR, 2, 18)): "水瓶座",
    (datetime(YEAR, 2, 19), datetime(YEAR, 3, 20)): "魚座",
    (datetime(YEAR, 3, 21), datetime(YEAR, 4, 19)): "牡羊座",
    (datetime(YEAR, 4, 20), datetime(YEAR, 5, 20)): "牡牛座",
    (datetime(YEAR, 5, 21), datetime(YEAR, 6, 21)): "双子座",
    (datetime(YEAR, 6, 22), datetime(YEAR, 7, 22)): "蟹座",
    (datetime(YEAR, 7, 23), datetime(YEAR, 8, 22)): "獅子座",
    (datetime(YEAR, 8, 23), datetime(YEAR, 9, 22)): "乙女座",
    (datetime(YEAR, 9, 23), datetime(YEAR, 10, 23)): "天秤座",
    (datetime(YEAR, 10, 24), datetime(YEAR, 11, 22)): "蠍座",
    (datetime(YEAR, 11, 23), datetime(YEAR, 12, 21)): "射手座",
    (datetime(YEAR, 12, 22), datetime(YEAR, 1, 19)): "山羊座",
}


def judge_zodiac_sign(month, day) -> str:
    target = datetime(YEAR, month, day)
    for key, value in ZODIAC_SIGNS.items():
        start, end = key
        if target >= start and target <= end:
            return value
    return ""


def main():
    fire.Fire({"judge": judge_zodiac_sign})


if __name__ == "__main__":
    main()
