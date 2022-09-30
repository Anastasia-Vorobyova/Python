# #Задайте список из нескольких чисел. 
# # Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def odd_position(my_list):
    count = 0
    for i in range(len(my_list)):
            if i%2 != 0:
                count += my_list[i]
    print(f'Сумма элементов равна: {count}')

my_list = [1,2,3,4,5,6,7,8,9,10]
odd_position(my_list) 
