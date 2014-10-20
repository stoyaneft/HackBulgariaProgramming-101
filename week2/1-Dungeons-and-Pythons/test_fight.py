import unittest

from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class TestFight(unittest.TestCase):

    def setUp(self):
        self.hero = Hero('Stoyan', 200, 'DeathBringer')
        self.hero.equip_weapon(Weapon('Sword', 20, 0.5))
        self.orc = Orc('Beginner Orc', 100, 1.5)
        self.orc.equip_weapon(Weapon('Stick', 10, 0.1))
        self.legendary_orc = Orc('Broksiguar', 200, 2)
        self.legendary_orc.equip_weapon(Weapon('Frostmourne', 80, 0.9))
        self.fight_hero_vs_orc = Fight(self.hero, self.orc)
        self.fight_hero_vs_legendary_orc = Fight(self.hero, self.legendary_orc)

    def test_fight_init(self):
        self.assertEqual(self.fight_hero_vs_orc.hero, self.hero)
        self.assertEqual(self.fight_hero_vs_orc.orc, self.orc)

    def test_simulate_hero_win(self):
        self.fight_hero_vs_orc.simulate_fight()
        self.assertEqual(self.fight_hero_vs_orc.orc.current_health, 0)

    def test_simulate_orc_win(self):
        self.fight_hero_vs_legendary_orc.simulate_fight()
        self.assertEqual(
            self.fight_hero_vs_legendary_orc.hero.current_health, 0)


if __name__ == '__main__':
    unittest.main()
