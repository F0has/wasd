meters = float(input("Введите количество метров"))
miles = meters / 1609
inches = meters / 39.37
yards = meters / 1.094
f = input("Перевести в мили, дюймы или ярды?")
if f == "Мили":
    print (miles)
if f == "Дюймы":
    print (inches)
if f == "Ярды":
    print (yards)

