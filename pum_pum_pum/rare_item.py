items = {
    "Телефон": frozenset({"техника", "электроника"}),
    "Самурайский меч": frozenset({"редкое", "оружие"}),
}


# Функция поиска по категории
def find_by_category(cat):
    result = []
    for name, cats in items.items():
        if cat in cats:
            result.append(name)
    return result


# Основной цикл
while True:
    print("\n1. Добавить товар")
    print("2. Показать все товары")
    print("3. Найти по категории")
    print("4. Выход")

    choice = input("Выберите: ")

    if choice == "1":
        name = input("Название товара: ")
        cats = input("Категории через запятую: ")
        categories = {c.strip().lower() for c in cats.split(",")}
        items[name] = frozenset(categories)

    elif choice == "2":
        print("\nВсе товары:")
        # Сортировка по длине названия
        for name, cats in sorted(items.items(), key=lambda x: len(x[0])):
            print(f"{name} -> {', '.join(cats)}")

    elif choice == "3":
        cat = input("Категория: ").lower()
        found = find_by_category(cat)
        if found:
            print(f"Найдено: {', '.join(found)}")
        else:
            print("Ничего не найдено")

    elif choice == "4":
        break