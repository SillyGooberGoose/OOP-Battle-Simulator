from random import randint
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        # Create the Hero's attributes here.
        self.name = name
        self.health = randint(100,150)
        self.attack_power = randint(10,25)

    def attack(self):
        # Return a random value from 1 through this Hero's attack power.
        return randint(1, self.attack_power)

    def take_damage(self, damage):
        # Subtract damage, but do not allow health to fall below 0.
        self.health = max(1, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        # Return a Boolean based on this Hero's health.
        return self.health > 0
    
    def battle_cry(self):
        # Returns a randomly generated battle cry.
        choosingPhrase = randint(1,4)
        if choosingPhrase == 1:
            print("I'll beat you with calculus!")
        elif choosingPhrase == 2:
            print("a + b = your demise!")
        elif choosingPhrase == 3:
            print("I can learn math while beating you up!")
        else:
            print("I can't think of anything funny!")