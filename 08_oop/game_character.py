# Game Character Design: base class with specialized subclasses

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks!")

    def show_status(self):
        print(f"{self.name} | Health: {self.health}")

class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a mighty sword! (damage 25)")

class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a fireball! (damage 40)")

class Archer(Character):
    def attack(self):
        print(f"{self.name} shoots an arrow from afar! (damage 20)")

team = [Warrior("Thor", 150), Mage("Merlin", 80), Archer("Legolas", 100)]
for hero in team:
    hero.show_status()
    hero.attack()
    print()
