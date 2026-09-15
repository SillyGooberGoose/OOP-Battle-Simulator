from goblin import Goblin
from hero import Hero
from time import sleep

ARENA_NAME = "The Golden Sphere"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

        if hero.is_alive():
            print(f"{hero.name} wins!")
        else:
            print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    badguy = Goblin("George")
    badguy2 = Goblin("Harold")
    print(f"{badguy.name} enters the arena with {badguy.health} health.")
    print(f"{badguy2.name} enters the arena with {badguy2.health} health.")

    print("But no hero has answered the call... yet.")
    sleep(2)

    coolguy = Hero("Mr. Bohon")
    heroPhrase = coolguy.battle_cry()

    print(f"{coolguy.name} enters the arena with {coolguy.health} health!")
    sleep(1)
    print(heroPhrase)
    print(f"{coolguy.name} ignites the battle with a sudden attack!")
    sleep(0.5)
    print(f"{coolguy.name} attackes {badguy.name}!")
    battle(coolguy, badguy)

if __name__ == "__main__":
    main()
