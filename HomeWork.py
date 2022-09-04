#Задание 1

a = str(input('введите число: '))
b = a.replace('.', '')
int_list = list(int(x) for x in b)
print(sum(int_list))
print('Конец задания №1')

#Задание 2

from math import factorial

n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
list2 = list( f(i) for i in range(1, n +1))
print(list2)
print('Конец задания №2')

#Задание 3

#import random
#print(random.shuffle(some_list))
some_list = list(map(int, input('введите числа через пробел: ').split()))

k = -1

for i in range(len(some_list)//2):
    some_list[k],some_list[i]=some_list[i],some_list[k]
    k -= 1
    print(some_list)    

print('Конец задания №3')