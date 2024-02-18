"""Рекурсивная функция"""
def fibonacci(input_number):
    """Функция находит конечное число"""
    if input_number in (1, 2):
        return 1
    return fibonacci(input_number - 1) + fibonacci(input_number - 2)

if __name__ == '__main__':
    input_number = int(input('Введите любое число'))
    print(fibonacci(input_number))
