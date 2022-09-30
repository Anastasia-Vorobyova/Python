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

#Задача 4: Алгоритм работает, если позиций две. 
# А по условию, требуется ввод неограниченного числа позиций, 
# через пробел, одной строкой. Ради практики, рекомендую доработай решение.
# Почитай про метод ".split()": https://inlnk.ru/Qwm0Pg