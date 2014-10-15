class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for note in money:
            self.money[note] += money[note]

    def total(self):
        total_money = sum(self.money.values())
        return total_money

    def can_withdraw_money(self, amount_of_money):

