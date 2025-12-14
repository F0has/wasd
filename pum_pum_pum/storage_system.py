products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80)],
    "Овощи": [("Морковь", 20, 30), ("Картофель", 50, 25)],
    "Напитки": [("Вода", 100, 20), ("Сок", 30, 100)]
}

print("Все товары:")
for category, items in products.items():
    print(f"\n{category}:")
    for name, count, price in items:
        print(f"  {name} — {count} шт., {price} руб.")

most_expensive = None
for category, items in products.items():
    for item in items:
        if most_expensive is None or item[2] > most_expensive[2]:
            most_expensive = item
            most_expensive_cat = category

print(f"\nСамый дорогой товар: {most_expensive[0]}, {most_expensive[2]} руб. (из {most_expensive_cat})")

max_count = 0
max_cat = ""
for category, items in products.items():
    total = sum(count for _, count, _ in items)
    if total > max_count:
        max_count = total
        max_cat = category

print(f"\nКатегория с наибольшим количеством товаров: {max_cat} ({max_count} шт.)")

total_cost = 0
for _, items in products.items():
    for name, count, price in items:
        total_cost += count * price

print(f"\nОбщая стоимость всех товаров: {total_cost} руб.")