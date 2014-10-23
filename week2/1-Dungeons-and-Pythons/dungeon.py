from orc import Orc
from fight import Fight


class Dungeon:

    def __init__(self, filename):
        self.filename = filename
        self.players = {}
        self.occupied_cells = {}
        with open(self.filename, 'r') as map_file:
            self.map_string = map_file.read()
        self.map_grid = [list(line) for line in self.map_string.split('\n')]

    def print_map(self):
        with open(self.filename, 'r') as map_file:
            self.map_string = map_file.read()
        print()
        print(self.map_string)
        return self.map_string

    @staticmethod
    def _get_entity_symbol(entity):
        if isinstance(entity, Orc):
            return 'O'
        else:
            return 'H'

    def spawn(self, player_name, entity):

        with open(self.filename, 'r') as map_file:
            self.map_string = map_file.read()
        for i, row in enumerate(self.map_grid):
            if 'S' in row:
                map_symbol = Dungeon._get_entity_symbol(entity)
                row_str = ''.join(row)
                row_str = row_str.replace('S', map_symbol, 1)
                self.map_string = self.map_string.replace('S', map_symbol, 1)
                entity_pos = [row_str.index(map_symbol), i]
                self.map_grid[entity_pos[1]][entity_pos[0]] = map_symbol
                self.players[player_name] = [entity, entity_pos]
                self.occupied_cells[tuple(entity_pos)] = entity
                self._update_map()
                return True
        return False

    def _check_move_possible(self, player_pos, direction):
        new_pos = list(player_pos)
        if direction == 'right':
            new_pos[0] += 1
        elif direction == 'left':
            new_pos[0] -= 1
        elif direction == 'up':
            new_pos[1] -= 1
        elif direction == 'down':
            new_pos[1] += 1
        if new_pos[0] < 0 or new_pos[0] > len(
                self.map_grid[0]) or new_pos[1] < 0 or new_pos[1] > len(
                self.map_grid):
            return (False, player_pos)
        if self.map_grid[new_pos[1]][new_pos[0]] == '#':
            return (False, player_pos)
        return (True, new_pos)

    def _update_map(self):
        rows = []
        for row in self.map_grid:
            rows.append(''.join(row))
        with open(self.filename, 'w') as map_file:
            map_file.write('\n'.join(rows))

    def move(self, player_name, direction):
        player = self.players[player_name]
        old_player_pos = list(player[1])
        is_move_correct, new_player_pos = self._check_move_possible(
            old_player_pos, direction)
        self.players[player_name][1] = new_player_pos
        if is_move_correct:
            old_row = old_player_pos[1]
            old_col = old_player_pos[0]
            self.map_grid[old_row][old_col] = '.'
            del self.occupied_cells[tuple(old_player_pos)]
            new_row = new_player_pos[1]
            new_col = new_player_pos[0]
            if self.map_grid[new_row][new_col] != '.':
                attacker = player[0]
                defender = self.occupied_cells[tuple(new_player_pos)]
                fight = Fight(attacker, defender)
                fight.simulate_fight()
                if not fight.attacker.is_alive():
                    self._update_map()
                    return True
            self.occupied_cells[tuple(new_player_pos)] = player[0]
            self.map_grid[new_row][new_col] = Dungeon._get_entity_symbol(
                player[0])
            self._update_map()
        return is_move_correct
