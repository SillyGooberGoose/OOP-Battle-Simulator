from enemy import Enemy
from random import randint

class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=250, attack_power=30)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} unleashes a crushing blow!")
        attackStyle = randint(1,2)
        if attackStyle == 1:
            print("FIREBALL!!!")
            return 5 * damage + bonus_damage
        else:
            print("EXCEL!!!!")
            return self.attack_power * randint(1,2)

    def take_damage(self, damage):
        damage = damage * 0.75
        super().take_damage(damage)

    def introduction(self):
        print("The ground shakes violently.....")
        print("Out comes the strongest man in history....")
        print("THE EXCEL LORD HIMSELF!!!")
        print(f"{self.name}!")