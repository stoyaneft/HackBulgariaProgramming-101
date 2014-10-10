def number_of_spams(number):
    power = 0
    while number % 3 == 0:
        power += 1
        number //= 3
    return power


def prepare_meal(number):
    spams = ['spam'] * number_of_spams(number)
    meal = ' '.join(spams)
    if number % 5 == 0:
        if spams:
            meal += " and "
        meal += 'eggs'
    return meal


def main():
    print(prepare_meal(5))

if __name__ == '__main__':
    main()
