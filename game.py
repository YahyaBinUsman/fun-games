import random

class Player:
    def __init__(self, health=100):
        self.health = health
        self.weapon = None

    def choose_weapon(self):
        print("Choose your weapon:")
        print("1. Sword")
        print("2. Bow and Arrow")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            self.weapon = Sword()
        elif choice == "2":
            self.weapon = BowAndArrow()
        else:
            print("Invalid choice. Defaulting to Sword.")
            self.weapon = Sword()

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount
        print(f"You gained {amount} health!")

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

class Sword:
    def __init__(self):
        self.damage = 20

class BowAndArrow:
    def __init__(self):
        self.damage = 15

def fight(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print("\nPlayer Health:", player.health)
        print(f"{enemy.name} Health:", enemy.health)

        action = input("Do you want to [1] Attack or [2] Give up? ")

        if action == "1":
            damage_dealt = player.weapon.damage
            enemy.take_damage(damage_dealt)
            print(f"You dealt {damage_dealt} damage to {enemy.name}!")

            damage_taken = random.randint(8, 18)  # Increased damage taken by enemies
            player.take_damage(damage_taken)
            print(f"{enemy.name} dealt {damage_taken} damage to you!")

        elif action == "2":
            print("You gave up. Game over!")
            player.health = 0

        else:
            print("Invalid action. Please choose '1' to Attack or '2' to Give up.")

    if player.is_alive():
        player.heal(random.randint(10, 20))  # Player gains random healing after defeating an enemy
        print("Congratulations! You Won the game by defeating the ", enemy.name)
    else:
        print("Game over! You were defeated by", enemy.name)

# Game setup
player = Player()
player.choose_weapon()

enemies = [
    Enemy("Goblin", 40, 12),  # Adjusted enemy health and damage values
    Enemy("Orc", 50, 18),
    Enemy("Dragon", 70, 25)
]

for enemy in enemies:
    print(f"\nA wild {enemy.name} appears!")
    fight(player, enemy)