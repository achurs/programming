import random

a = [['hi',0],['bye',0]]

n = a.__len__()
print(n)

for i in range(1000):
    randnum = random.random()
    flag = True
    x=1
    count = 0
    while(flag):
        if(randnum < x/n):
            a[count][1] += 1
            flag = False
        else:
            x += 1
            count += 1

print(a)