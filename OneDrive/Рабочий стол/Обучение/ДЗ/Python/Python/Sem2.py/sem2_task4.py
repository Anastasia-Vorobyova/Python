#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint
list = int(input('Введите число элемента: '))
numbers = []
for i in range(list):
    numbers.append(randint(-list,list))
print(numbers)

a = int(input('Введите позицию первого элемента: '))
b = int(input('Введите позицию второго элемента: '))
for i in range(len(numbers)):
    multiplication = numbers[a -1] * numbers[b - 1]
print(f'Произведение элементов: {numbers[a -1]} * {numbers[b -1]} =', multiplication)