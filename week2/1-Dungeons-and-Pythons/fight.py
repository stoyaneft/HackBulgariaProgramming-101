from random import randint


class Fight:

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def simulate_fight(self):
        roll = randint(0, 1)
        PLAYERS = (self.hero, self.orc)
        current_player = roll
        print()
        print('{} starts the fight.'.format(PLAYERS[roll].name))
        while self.hero.current_health != 0 and self.orc.current_health != 0:
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
        if not self.hero.health:
            print('{} wins!'.format(self.hero.name))
        else:
            print('{} wins!'.format(self.orc.name))
