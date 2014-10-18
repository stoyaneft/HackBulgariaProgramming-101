def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


def simplify_fraction(fraction):
    x, y = fraction[0], fraction[1]
    greatest_divisor = gcd(x, y)
    simplified_fraction = x // greatest_divisor, y // greatest_divisor
    return simplified_fraction
