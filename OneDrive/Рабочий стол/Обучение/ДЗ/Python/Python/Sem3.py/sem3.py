#1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# import time

# def my_random(minn, maxx):
#     time.sleep(0.3)
#     return int((time.time() % 1  * (maxx - minn)) + minn)
# #                     0.9                  7           1

# for i in range(10):
#     print(my_random(1, 9))

# or
# def random(a,b):
#     the_set = set()
#     list = []
#     for i in range(a,b):
#         the_set.add(str(i))

#     for e in the_set:
#         list.append(e)
#     print(list)

# random(5, 10)

# or:
# def random():
#     interval = int(input('Введите желаемый интервал рандома: '))
#     ms = time.time()*1000.0
#     b = int(ms)
#     d = ms - b
#     answer = d * interval
#     print(int(round(answer, 0)))
#     return answer

# random()

# а если нужно одино число:
# def random(a,b):
#     the_set = set()
#     list = []
#     for i in range(a,b):
#         the_set.add(str(i))
#     for e in the_set:
#         list.append(e)
#         break
#     print(list)

# random(5, 10)

#2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['efg23', '79234gefg', 'sdgs', 'g53']
# '2'
# ['efg23', '79234gefg']

# list = ['efg23', '79234gefg', 'sdgs', 'g53']

# def func(x):
#     count = 0
#     for i in range(0, len(list)):
#         if x in list[i]:
#             count += 1
#     print(count)

# x = input('Введите что ищем: ')
# func(x)
#Or
# list1 = ['efg23', '79234gefg', 'sdgs', 'g53']

# def func(list, x):
#     count = 0
#     for i in range(0, len(list)):
#         if x in list[i]:
#             count += 1
#     print(count)

# x = input('Введите что ищем: ')
# func(list1, x)

# or
# def my_list(list, p):
#     count.append i
#     for i in list:
#         if p in i:
#             count += 1
#     return count

# list = ['efg23', '79234gefg', 'sdgs', 'g53']
# p = '2'
# print(my_list(list, p))

# 3. Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1
# list = ["qwe", "asd", "qwe", "zxc", "qwe", "ertqwe"]
# x = 'qwe'
# def Entry(list, x):
#     count = 0
#     for i in range(0, len(list)):
#         if x in list[i]:
#             count += 1
#             if count == 2:
#                 print(i)
    
# Entry(list, x)

# or
# def findstr(my_list: list, find_string: str) -> int:
#     count = 0
#     for i in range(len(my_list)):
#         if find_string == my_list[i]:
#             count += 1
#             if count == 2:
#                 return i
#     return -1

# list_find = ["йцу", "фыв","йцу", "ячс", "цук", "йцукен"]
# find_string = "йцу"

# print(findstr(list_find, find_string))



#5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# i = int(input('Введите число: '))
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) - fib(n-2)
# list=[]
# for e in range(1,10):
#     list.append(fib(e))
# print(list)
