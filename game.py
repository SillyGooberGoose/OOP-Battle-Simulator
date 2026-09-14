from goblin import Goblin
from hero import Hero
from time import sleep

ARENA_NAME = "The Golden Sphere"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("George")
    goblinTwo = Goblin("Harold")
    goblinDamage = goblin.attack()
    goblinTwoDamage = goblinTwo.attack()
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    print("But no hero has answered the call... yet.")
    sleep(2)

    hero = Hero("Mr. Bohon")
    heroDamage = hero.attack()
    heroPhrase = hero.battle_cry()

    print(f"{hero.name} enters the arena with {hero.health} health!")
    sleep(1)
    print(heroPhrase)
    print(f"{hero.name} ignites the battle with a sudden attack!")

    sleep(0.5)
    print(f"{hero.name} attackes {goblin.name}!")
    sleep(1)
    goblin.take_damage(heroDamage)

    sleep(0.75)
    print(f"{goblin.name} gets mad and attacks {hero.name}!")
    hero.take_damage(goblinDamage)

if __name__ == "__main__":
    main()
