import unittest

from orc import Orc
from weapon import Weapon


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.orc = Orc('Broks', 100, 1.5)

    def test_orc_init_berserk(self):
        self.assertEqual(self.orc.berserk_factor, 1.5)

    def test_orc_attack_without_weapon(self):
        self.assertEqual(self.orc.attack(), 0)

    def test_orc_attack_with_weapon(self):
        axe = Weapon('Axe', 25, 0.5)
        self.orc.equip_weapon(axe)
        self.assertEqual(self.orc.attack(), 25*1.5)

if __name__ == '__main__':
    unittest.main()
