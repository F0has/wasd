text = input("Введите строку: ")
cleaned = ''.join(text.lower().split())
if cleaned == cleaned[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")
