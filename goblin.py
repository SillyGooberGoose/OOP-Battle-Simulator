from random import randint

from enemy import Enemy


class Goblin(Enemy):
    """A basic enemy found in the arena."""

    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.gold = 0

    def stealGold(self, hero):
        """GOBBOS TAKIN HEROS GOLD."""
        self.gold = self.gold + hero.gold
        hero.gold = 0
        print("GIT REKT NOOB")
