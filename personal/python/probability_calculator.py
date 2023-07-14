import random
from tqdm import tqdm

number = int(input("How many numbers?:"))
a = []
for i in range(number):
    choice = input("Enter your choice:")
    a.append([choice,0])

n = a.__len__()
print(n)

for i in tqdm(range(100000000)):
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

for i in range(number):
    print(a[i][0],a[i][1])
