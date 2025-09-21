numbers = input("Enter numbers ")
product = 1
for digit in numbers:
    product *= int(digit)
    print(product)
