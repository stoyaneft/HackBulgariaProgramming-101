from hero import Hero

import unittest


class TestHero(unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init_nickname(self):
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.bron_hero.known_as(), 'Bron the DragonSlayer')


if __name__ == '__main__':
    unittest.main()
