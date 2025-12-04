numbers = int(input("Введите начало диапазона"))
numbers2 = int(input("Введите конец диапазона"))
for i in range(numbers, numbers2 + 1):
    for j in range(11):
        print(i * j)