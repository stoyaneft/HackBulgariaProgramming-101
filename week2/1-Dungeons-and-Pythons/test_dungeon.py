from os import remove
import unittest

from dungeon import Dungeon
from hero import Hero
from orc import Orc
from weapon import Weapon


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.start_map_content = 'S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S'
        with open('basic_dungeon.txt', 'w') as map_file:
            map_file.write(self.start_map_content)
        self.map = Dungeon('basic_dungeon.txt')
        self.hero_player = Hero('Stoyan', 100, 'DeathBringer')
        self.hero_player.equip_weapon(Weapon('Sword', 20, 0.5))
        self.orc_player = Orc('Broks', 100, 1.5)
        self.orc_player.equip_weapon(Weapon('Stick', 10, 0.1))
        self.battle_map_content = 'S.#\n#S#'
        with open('battle_map.txt', 'w') as map_file:
            map_file.write(self.battle_map_content)
        self.battle_map = Dungeon('battle_map.txt')
        self.battle_map.spawn('human', self.hero_player)
        self.battle_map.spawn('orc', self.orc_player)

    def tearDown(self):
        remove(self.map.filename)
        remove('battle_map.txt')

    def test_dungeon_init(self):
        self.assertEqual(self.map.filename, 'basic_dungeon.txt')

    def test_print_map(self):
        self.assertEqual(self.map.print_map(), self.start_map_content)

    def test_first_spawn_succesful(self):
        self.assertTrue(self.map.spawn('player_1', self.hero_player))

    def is_map_changed_after_spawning_entity(self, entity, symbol):
        self.map.spawn('player', entity)
        with open(self.map.filename, 'r') as map_file:
            map_content_after_spawn = map_file.read()
        return map_content_after_spawn == self.start_map_content.replace(
            'S', symbol, 1)

    def test_map_changed_after_spawning_hero(self):
        self.assertTrue(
            self.is_map_changed_after_spawning_entity(self.hero_player, 'H'))

    def test_map_changed_after_spawning_orc(self):
        self.assertTrue(
            self.is_map_changed_after_spawning_entity(self.orc_player, 'O'))

    def test_spawn_unsuccesful_on_full_map(self):
        self.map.spawn('player1', self.hero_player)
        self.map.spawn('player2', self.orc_player)
        self.assertFalse(self.map.spawn('player3', self.orc_player))

    def test_correct_move(self):
        self.map.spawn('player1', self.hero_player)
        self.assertTrue(self.map.move('player1', 'right'))

    def test_out_of_map_move(self):
        self.map.spawn('player1', self.hero_player)
        self.assertFalse(self.map.move('player1', 'left'))

    def test_move_through_obstacle(self):
        self.map.spawn('player1', self.hero_player)
        self.assertFalse(self.map.move('player1', 'down'))

    def test_move_reflected_on_map(self):
        self.map.spawn('player1', self.hero_player)
        self.map.spawn('player2', self.orc_player)
        self.map.move('player1', 'right')
        self.map.move('player1', 'down')
        self.map.move('player2', 'up')
        self.map.move('player2', 'up')
        self.assertEqual(
            self.map.print_map(),
            '..##......\n#H##..###.\n#.###.###O\n#.....###.\n###.#####.'
        )

    def test_move_into_battle(self):
        self.battle_map.move('human', 'right')
        self.battle_map.move('orc', 'up')
        player_dead = not self.hero_player.is_alive(
        ) or not self.orc_player.is_alive()
        self.assertTrue(player_dead)

    def test_map_accurate_after_battle(self):
        self.battle_map.move('human', 'right')
        self.battle_map.move('orc', 'up')
        self.assertEqual(self.battle_map.print_map(), '.H#\n#.#')

if __name__ == '__main__':
    unittest.main()
