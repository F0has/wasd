num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
my_list = [num1, num2, num3]
max_num = max(my_list)
min_num = min(my_list)
arithmetic_mean = ((num1 + num2 + num3) / 3)
a = input("Максимальное, Минимальное или Среднее арефметическое?")
if a == "Максимальное":
    print (max_num)
if a == "Минимальное":
    print (min_num)
if a == "Среднее арефметическое":
    print (arithmetic_mean)