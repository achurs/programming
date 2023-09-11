
n = int(input("Enter a the total numbers of users: "))
mydict = {}
for i in range(n):
    name = input("Enter your name: ")
    number = int(input("Enter your number: "))
    mydict[name] = number

check = input("Enter the name to be looked up: ")
if check in mydict:
    print(mydict[check])