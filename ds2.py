# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random 
N = int(input('Введите число N '))
a=[]
result = []
for i in range(N):
    a.append(random.randint(-50, 50))
print (a)

if len(a) % 2 == 0:
    num = int(len(a)/2)
else:
    num = int(len(a)/2) + 1
for i in range(num):
    res = a[i]*a[-i-1]
    result.append(res)
print(result)