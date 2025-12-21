def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функция {func.__name__} вызвана {wrapper.count} раз")
        print(f"Аргументы: {args}")
        result = func(*args, **kwargs)
        print(result)
        return result
    wrapper.count = 0
    return wrapper
@call_counter
def add(a, b):
    return a + b
@call_counter
def repeat(text, n):
    return text * n
