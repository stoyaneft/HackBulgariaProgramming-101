class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for note in money:
            self.money[note] += money[note]

    def total(self):
        total_money = 0
        for note in self.money:
            total_money += note * self.money[note]
        return total_money

    @staticmethod
    def subset_sum(numbers, sum, index):
        if sum == 0:
            return True
        if index >= len(numbers):
            return False
        else:
            return CashDesk.subset_sum(
                numbers, sum - numbers[index], index + 1
            ) or CashDesk.subset_sum(numbers, sum, index + 1)

    def can_withdraw_money(self, amount_of_money):
        money_list = []
        for note in self.money:
            for i in range(self.money[note]):
                money_list.append(note)
        return CashDesk.subset_sum(money_list, amount_of_money, 0)
