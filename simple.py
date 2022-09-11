#f = open ('file.txt', 'w')
#l =  ['1', '2', '3', '5', '8', '15', '23', '38']
#for i in l:
#    f.write(i+' ')

#f.close    
f = open ('file.txt', 'r')
l = [line.split() for line in f]

list1 = list(int(i) for i in l)
print(list1)    

def f(x):
    return x**2

for i in list1:
    if i%2 == 0:
        list2 = [(f(i), i)]

print(list2)