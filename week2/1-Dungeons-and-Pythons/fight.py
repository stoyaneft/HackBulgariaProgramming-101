from random import randint


class Fight:

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def simulate_fight(self):
        roll = randint(0, 1)
        PLAYERS = (self.attacker, self.defender)
        current_player = roll
        print()
        print('{} starts the fight.'.format(PLAYERS[roll].name))
        while self.attacker.is_alive() and self.defender.is_alive():
            damage = PLAYERS[current_player].attack()
            other_player = (current_player + 1) % 2
            print('{} does {} damage to {}.'.format(
                PLAYERS[current_player].name,
                damage, PLAYERS[other_player].name))
            PLAYERS[other_player].take_damage(damage)
            print('{} health is now {}.'.format(
                PLAYERS[other_player].name,
                PLAYERS[other_player].current_health))
            current_player = other_player
        winner = (current_player + 1) % 2
        print('{} wins!'.format(PLAYERS[winner].name))
