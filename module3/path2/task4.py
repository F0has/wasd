numbers = []
while True:
    num = int(input("Введите число: "))
    if num == 7:
        print("Good bye!")
        break
    numbers.append(num)
if numbers:
    print(f"Сумма: {sum(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Минимум: {min(numbers)}")
else:
    print("Не было введено ни одного числа (кроме 7)")