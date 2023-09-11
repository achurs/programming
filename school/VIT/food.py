def sep(list_1,list_2):
    food_list = []
    drinks_list = []
    #if the list_2 contains the value 1 print the respective index in list_1
    for i in range(len(list_1)):
        if list_2[i] == 1:
            food_list.append(list_1[i])
        else:
            drinks_list.append(list_1[i])
    return food_list,drinks_list

#main
first_list = ['bread','water','sandwich']
secons_list = [1,0,1]
sor_list = sep(first_list,secons_list)
print(sor_list)