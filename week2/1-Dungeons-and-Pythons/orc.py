from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if berserk_factor > 2:
            berserk_factor = 2
        elif berserk_factor < 1:
            berserk_factor = 1
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
            if not self.has_weapon():
                return 0
            else:
                return self.weapon.damage * self.berserk_factor
