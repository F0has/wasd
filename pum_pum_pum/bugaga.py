import os


def load_notes():
    """Читает заметки из файла и возвращает список кортежей"""
    notes = []
    if not os.path.exists("notes.txt"):
        return notes

    with open("notes.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "|" in line:
                parts = line.split("|", 1)
                if len(parts) == 2:
                    category = parts[0].strip()
                    text = parts[1].strip()
                    notes.append((category, text))
    return notes


def save_notes(notes):
    """Сохраняет все заметки в файл"""
    with open("notes.txt", "w", encoding="utf-8") as f:
        for category, text in notes:
            f.write(f"{category} | {text}\n")


def add_note():
    """Добавляет новую заметку в файл"""
    category = input("Введите категорию: ").strip()
    text = input("Введите текст заметки: ").strip()

    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(f"{category} | {text}\n")
    print("Заметка добавлена!")


def find_by_category():
    """Находит все заметки указанной категории"""
    category = input("Введите категорию для поиска: ").strip()
    notes = load_notes()

    print(f"\nЗаметки в категории '{category}':")
    found = False
    for cat, text in notes:
        if cat.lower() == category.lower():
            print(f"  - {text}")
            found = True

    if not found:
        print("  Не найдено")


def search_word():
    """Ищет заметки, содержащие указанное слово"""
    word = input("Введите слово для поиска: ").strip().lower()
    notes = load_notes()

    print(f"\nЗаметки со словом '{word}':")
    found = False
    for category, text in notes:
        if word in category.lower() or word in text.lower():
            print(f"  [{category}] - {text}")
            found = True

    if not found:
        print("  Не найдено")


def main():
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Найти по категории")
        print("4. Поиск по слову")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            notes = load_notes()
            if notes:
                print("\nВсе заметки:")
                for i, (category, text) in enumerate(notes, 1):
                    print(f"{i}. [{category}] - {text}")
            else:
                print("\nЗаметок нет")
        elif choice == "3":
            find_by_category()
        elif choice == "4":
            search_word()
        elif choice == "5":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()