def what_is_my_sign(day, month):
    ZODIAC_SIGNS = (
        "Capricorn", "Aquarius", "Pisces", "Aries",
        "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"
    )
    MONTH_DIVIDERS = {1: 20, 2: 19, 3: 21, 4: 21, 5: 21,
                      6: 21, 7: 22, 8: 23, 9: 23, 10: 23, 11: 22, 12: 22}
    if day >= MONTH_DIVIDERS[month]:
        return ZODIAC_SIGNS[month]
    else:
        return ZODIAC_SIGNS[month - 1]


def main():
    print(what_is_my_sign(27, 3))


if __name__ == '__main__':
    main()
