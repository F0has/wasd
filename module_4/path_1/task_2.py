text = input("Введите текст: ")
words_input = input("Введите зарезервированные слова через пробел: ")
reserved_words = words_input.split()
for word in reserved_words:
    text = text.replace(word, word.upper())
print("Измененный текст:")
print(text)