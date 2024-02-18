def degree(n: int):
    """
    Проверяет является ли число степенью двойки
    """
    while n % 2 == 0 and n != 0:
        n //= 2
    print(n == 1)

if __name__ == '__main__':
    n = int(input('Введите любое число '))
    degree(n)
