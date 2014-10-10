def calculate_coins(sum):
    sum *= 100
    coins = [100, 50, 20, 10, 5, 2, 1]
    calculated_coins = {}
    count = 0
    for coin in coins:
        count = sum // coin
        calculated_coins[coin] = int(count)
        if count:
            sum %= coin
    return calculated_coins


def main():
    print(calculate_coins(8.94))


if __name__ == '__main__':
    main()
