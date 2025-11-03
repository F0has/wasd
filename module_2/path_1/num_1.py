num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
a = num1 + num2 + num3
b = num1 * num2 * num3
c = (input("Сумма или Произведение?"))
if c == "Сумма":
    print(a)
else: c = "Произведение"
print(b)
