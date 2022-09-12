#Case 1

def factor(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result

print(factor(100))

#Case 2

def repeat_kill(list_numbers):
    result = []
    result.append(list_numbers[0])
    for num in list_numbers:
        for resNum in result:
            if num != resNum and resNum == result[-1]:
                result.append(num)
            if num == resNum:
                break
    return  result

print(repeat_kill([1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10]))

#Case 3
import random

def save_data(some_data):
    with open('file.txt', 'w') as data:
        data.write(some_data)

def poly_list(k):
    result = ''
    for i in range(k, -1, -1):
        a = random.randint(0, 101)
        if a == 0:
            result += str(a)
            break
        else:
            result += str(a) + '*x'
        if i > 1:
            result += '^{}'.format(i)
        result += ' + '      
    result += '0'
    result += ' = 0'
    save_data(result)
    return result                    

print(poly_list(3))