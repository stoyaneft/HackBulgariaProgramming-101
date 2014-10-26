import unittest

from weapon import Weapon


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.sword = Weapon('Sword', 15, 0.4)

    def test_init_weapon(self):
        self.assertEqual(self.sword.type, 'Sword')
        self.assertEqual(self.sword.damage, 15)
        self.assertEqual(self.sword.critical_strike_percent, 0.4)

    def test_critical_hit(self):
        critical_hit_used = False
        critical_hit_not_used = False
        while True:
            if self.sword.critical_hit():
                critical_hit_used = True
                return
        while True:
            if not self.sword.critical_hit():
                critical_hit_not_used = True
                return
        self.assertTrue(critical_hit_used)
        self.assertFalse(critical_hit_not_used)

    def test_critical_raises_error(self):
        with self.assertRaises(ValueError):
            axe = Weapon('Axe', 25, 2)

if __name__ == '__main__':
    unittest.main()
