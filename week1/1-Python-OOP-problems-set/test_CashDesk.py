import unittest

from CashDesk import CashDesk


class CashDeskTest(unittest.TestCase):

    def setUp(self):
        self.cash_desk = CashDesk()

    def test_cashdesk_empty_when_created(self):
        self.assertEqual(
            self.cash_desk.money, {100: 0, 50: 0, 20: 0, 10: 0,
                                   5: 0, 2: 0, 1: 0})
        self.assertEqual(self.cash_desk.total(), 0)

    def test_take_money(self):
        self.cash_desk.take_money({1: 2, 50: 1, 20: 1})
        self.assertEqual(self.cash_desk.total(), 72)
        self.cash_desk.take_money({1: 1, 2: 1, 5: 1, 20: 1})
        self.assertEqual(self.cash_desk.total(), 100)

    def test_can_withdraw_money(self):
        self.cash_desk.take_money({50: 1, 100: 2})
        self.assertTrue(self.cash_desk.can_withdraw_money(250))
        self.assertTrue(self.cash_desk.can_withdraw_money(150))
        self.assertFalse(self.cash_desk.can_withdraw_money(70))
        self.assertFalse(self.cash_desk.can_withdraw_money(180))

if __name__ == '__main__':
    unittest.main()
