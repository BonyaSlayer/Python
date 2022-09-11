#Case 1

data = [1, 2, 3, 4, 5, 6, 7, 8]
data2 = data [1::2]
print(sum(data2))

#Case 2

def list_pars(list):
    result = []
    len_list = int(len(list)/2)
    for i in range(len_list):
        result.append(list[i]*list[- i - 1])
    return result

print(list_pars([1,5,6,7,8,9,10,8]))

#Case 3

def diff_of_num(list):
    min = list[0]
    max = 0
    list_res = []
    for i in list:
        res = round(i % 1, 10)
        if res != 0:
            list_res.append(res)
    for i in list_res:
        if i < min:
            min = i
        if i > max:
            max = i
    return max -min 

print(diff_of_num([1.8, 0.4, 1.055]))

#Case 4

n = int(input('Введите число: '))
 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b)

#Case 5
#Если я правильно понял отрицательбное число Фиббоначи можно получить записью a, b = -1, -1 , но как реализовать в список общий не понятно.

def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

fib_list = list(fib(8))
print(fib_list)
