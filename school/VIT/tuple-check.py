#check if all the elements are same in a tuple
tup = (1,1,1,2)
ele = tup[0]
flag = True
print(ele)
for i in tup:
    if i != ele:
        flag = False
        break
if flag:
    print("True")
else:
    print("False")