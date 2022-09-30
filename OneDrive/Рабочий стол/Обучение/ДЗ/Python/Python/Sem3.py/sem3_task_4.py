# #4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal_number = int(input('Введите десятичное число: '))

def find_number(decimal_number):
    b = ''
    while decimal_number > 0:
        b = str(decimal_number % 2) + b
        decimal_number = decimal_number // 2
    print(f"двоичное число {b}")

find_number(decimal_number)

