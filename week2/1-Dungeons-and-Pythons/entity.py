class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.current_health = health
        self.weapon = None

    def get_health(self):
        return self.current_health

    def is_alive(self):
        return self.current_health > 0

    def take_damage(self, damage_points):
        self.current_health -= damage_points
        if self.current_health < 0:
            self.current_health = 0

    def take_healing(self, healing_points):
        if self.current_health == 0:
            return False
        self.current_health += healing_points
        if self.current_health > self.health:
            self.current_health = self.health
        return True

    def has_weapon(self):
        return self.weapon is not None

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            if self.weapon.critical_hit():
                return self.weapon.damage * 2
            else:
                return self.weapon.damage
