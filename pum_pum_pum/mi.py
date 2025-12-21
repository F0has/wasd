def simple_file_analyzer():
    filename = input("Введите имя файла: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            line_count = len(lines)
            word_count = 0
            char_count = 0
            empty_count = 0

            for line in lines:
                char_count += len(line)
                words = line.split()
                word_count += len(words)
                if line.strip() == '':
                    empty_count += 1

            print(f"\nАнализ файла '{filename}':")
            print(f"Строк: {line_count}")
            print(f"Слов: {word_count}")
            print(f"Символов: {char_count}")
            print(f"Пустых строк: {empty_count}")

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден!")
    except PermissionError:
        print(f"Нет доступа к файлу '{filename}'")
    except Exception as e:
        print(f"Ошибка: {e}")


simple_file_analyzer()