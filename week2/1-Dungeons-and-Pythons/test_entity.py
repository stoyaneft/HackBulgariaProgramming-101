import unittest

from entity import Entity
from weapon import Weapon


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity = Entity('Name', 100)

    def test_entity_init(self):
        self.assertEqual(self.entity.name, 'Name')
        self.assertEqual(self.entity.health, 100)

    def test_get_health(self):
        self.assertEqual(
            self.entity.get_health(), self.entity.health)

    def test_is_alive(self):
        self.assertTrue(self.entity.is_alive())
        self.entity.current_health = 0
        self.assertFalse(self.entity.is_alive())

    def test_take_damage(self):
        self.entity.take_damage(50)
        self.assertEqual(self.entity.get_health(), 50)

    def test_take_damage_more_than_hp(self):
        self.entity.take_damage(120)
        self.assertEqual(self.entity.get_health(), 0)

    def test_take_healing_on_death_player(self):
        self.entity.take_damage(100)
        self.assertFalse(self.entity.take_healing(50))

    def test_take_healing_more_than_max_health(self):
        self.entity.take_damage(20)
        self.assertTrue(self.entity.take_healing(30))
        self.assertEqual(self.entity.get_health(), 100)

    def test_take_normal_healing(self):
        self.entity.take_damage(50)
        self.assertTrue(self.entity.take_healing(30))
        self.assertEqual(self.entity.get_health(), 80)

    def test_has_no_weapon(self):
        self.assertFalse(self.entity.has_weapon())

    def test_has_weapon(self):
        self.weapon = Weapon('Axe', 25, 0.5)

    def test_equip_weapon(self):
        axe = Weapon('Axe', 25, 0.5)
        self.entity.equip_weapon(axe)
        self.assertTrue(self.entity.has_weapon())

    def test_attack_without_weapon(self):
        self.assertEqual(self.entity.attack(), 0)

    def test_attack_with_weapon(self):
        axe = Weapon('Axe', 25, 0.5)
        self.entity.equip_weapon(axe)
        self.assertEqual(self.entity.attack(), 25)


if __name__ == '__main__':
    unittest.main()
