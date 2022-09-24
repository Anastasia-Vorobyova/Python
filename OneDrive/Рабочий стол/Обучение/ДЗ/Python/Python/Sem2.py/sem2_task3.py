#Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

num = int (input('Введите число: ')) 
def receive_sequence(num):
    return[round((1 + 1 / k)**k, 3) for k in range (1, num + 1)]

print(receive_sequence(num))
print(round(sum(receive_sequence(num))))
