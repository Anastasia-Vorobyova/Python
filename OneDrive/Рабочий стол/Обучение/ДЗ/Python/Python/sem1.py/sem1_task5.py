#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
x1 = int(input("Введите координату х1 "))
x2 = int(input("Введите координату х2 "))
y1 = int(input("Введите координату y1 "))
y2 = int(input("Введите координату y2 "))
delta_x = x1 - x2 
delta_y = y1 - y2
differents = 0
differents = (delta_x * delta_x) + (delta_y * delta_y)
sqrt = math.sqrt(differents)
print(f'расстояние между точками {sqrt}')