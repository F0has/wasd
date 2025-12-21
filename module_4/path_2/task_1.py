while True:
    expr = input("Введите выражение (например 23+12): ")

    if '+' in expr:
        a, b = expr.split('+')
        print(float(a) + float(b))
    elif '-' in expr:
        a, b = expr.split('-')
        print(float(a) - float(b))
    elif '*' in expr:
        a, b = expr.split('*')
        print(float(a) * float(b))
    elif '/' in expr:
        a, b = expr.split('/')
        if float(b) == 0:
            print("Ошибка: деление на ноль")
        else:
            print(float(a) / float(b))
    else:
        print("Нет знака операции (+, -, *, /)")

    again = input("Ещё раз? (да/нет): ")
    if again.lower() != 'да':
        break