#Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
#user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
# numbers = list(map(int, user_string))
# print(max(numbers), min(numbers))



# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 
# 1) с помощью математических формул нахождения корней квадратного уравнения D=bквадрат - 4ac 
#def square_root(a: int = 0, b: int = 0, c: int = 0) -> list:
#     discriminant = (b ** 2) - (4 * a * c)
#     if discriminant < 0:
#         return []
#     elif discriminant == 0:
#         x = - (b / (2 * a))
#         return [x]

#     x1 = (-b + sqrt(discriminant)) / (2 * a)
#     x2 = (-b - sqrt(discriminant)) / (2 * a)
#     return [x1, x2]
    
# print('Ax² + Bx + C = 0')
# a = int(input('A= '))
# b = int(input('B= '))
# c = int(input('C= '))
# print(square_root(a, b, c))


# 2) с помощью дополнительных библиотек Python



# Задайте два числа.
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# def calculate_NOK(x, y): 
#     if x > y: 
#         greater = x 
#     else:
#         greater = y 
#     while(True): 
#         if((greater % x == 0) and(greater % y == 0)): 
#             NOK = greater 
#             break 
#         greater += 1 
#     return NOK 
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: ")) 
# print("The N.O.K of", num1,"and", num2,"is", calculate_NOK(num1, num2))
#or
# a = int(input("a = "))
# b = int(input("b = "))
# i = min(a, b)
# while True:
#     if i%a==0 and i%b==0:
#         break
#     i += 1
# print(i)
#or
# a = int(input("Введите число A: "))
# b = int(input("Введите число B: "))

# def nok_value(a: int = 0, b: int = 0):

#     nok = 1
#     while ((nok % a) + (nok % b) != 0):
#         nok += 1
#     return nok

# print(nok_value(a, b))

#or
# def gcd (a,b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)
# a, b = map(int, input().split())
# print(a*b//gcd(a,b))

#def NOK(a, b):
#     for i in range(a, 10000, a):
#         for j in range(b, 10000, b):
#             if i == j:
#                 return(i)
# a = int(input('Введите А от 1 до 100:'))
# b = int(input('Введите B от 1 до 100:'))
# print(NOK(a, b))

# or
# def HOK(a, b):
#     i = min(a, b)
#     while True:
#         if i%a == 0 and i%b == 0:
#             break
#         i += 1
#     print(i) 


# # a = int(input("a = "))
# # b = int(input("b = "))
# # HOK(a,b)

# ordef NOD(a,b):
#     while True:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a

#         if a % b == 0:
#             return b
#         elif b % a == 0:
#             return a


# def NOK(a:int, b:int) -> int:
#         return int((a * b) / NOD(a,b))


# print(NOK(126, 70))

# or
# import math
# a = int(input("a = "))
# b = int(input("b = "))
# print(math.lcm(a, b))

