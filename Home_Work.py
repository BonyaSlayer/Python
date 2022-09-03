#Задание 1

x = int(input("x= "))
y = int(input("y= "))
if x>0 and y>0:
    print('I')
elif x<0 and y>0:
    print('II')
elif x<0 and y<0:
    print('III')
elif x>0 and y<0:
    print('IV')
print('Конец задания')

#Задание 2

cord = str(input('Укажите номер четверти: '))
i_values_x = list(range(10))
i_values_y = list(range(0, -10, -1)) 
if cord == 'I':
    print('x= ', i_values_x)
    print('y= ', i_values_x)
elif cord == 'II':
    print('x= ', i_values_y)
    print('y= ', i_values_x)
elif cord == 'III':
    print('x= ', i_values_y)
    print('y= ', i_values_y)
elif cord == 'IV':
    print('x= ', i_values_x)
    print('y= ', i_values_y)
print('Конец задания')

#Задание 3

import math
p1 = [2, 2]
p2 = [3, 3]
distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print(round(distance, 2))
print('Конец задания')

    
    