import random

numbers = [random.randint(-5, 5) for _ in range(10)]

print("Список:", numbers)
print("Минимум:", min(numbers))
print("Максимум:", max(numbers))
print("Положительных:", sum(1 for x in numbers if x > 0))
print("Отрицательных:", sum(1 for x in numbers if x < 0))
print("Нулей:", sum(1 for x in numbers if x == 0))