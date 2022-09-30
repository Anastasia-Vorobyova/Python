# #3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

def mulitiplyArray(my_list):
    max_number = 0
    min_number = 1
    for i in my_list:
            if (i - int(i)) < min_number:
                min_number = i - int(i)
            if (i - int(i)) > max_number:
                max_number = i - int(i)
    print(f"{max_number - min_number}")

my_list = [1.1, 1.2, 3.1, 10.01]
mulitiplyArray(my_list)
