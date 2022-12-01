# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random 
N = int(input('Введите число N '))
a=[]
b=[]
result = []
for i in range(N):
    a.append(random.uniform(0, 10))
print (a)
for i in range(len(a)):
    b.append(a[i]-int(a[i]))
print (b)
print ('Максимальный', format(max(b), '.3f'))
print ('Минимальный',format(min(b), '.3f'))
print ('Разность', format(max(b) - min(b), '.3f'))

