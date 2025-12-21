class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self):
        print(f"{self.name}: Персонаж атакует!")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Power: {self.power})"


class Warrior(Character):
    def attack(self):
        print(f"{self.name}: Воин наносит мощный удар мечом!")


class Mage(Character):
    def __init__(self, name, hp, power, mana):
        super().__init__(name, hp, power)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг выпускает огненный шар!")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Power: {self.power}, Mana: {self.mana})"


# Создаём персонажей
w = Warrior("Арагорн", 120, 20)
m = Mage("Гендальф", 80, 10, 200)

# Меню
characters = [w, m]

while True:
    print("\n1. Показать всех персонажей")
    print("2. Атаковать")
    print("3. Выход")

    choice = input("Выберите: ")

    if choice == "1":
        for char in characters:
            print(char)
    elif choice == "2":
        for char in characters:
            char.attack()
    elif choice == "3":
        break