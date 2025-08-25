list=[10,12,13,12,50,70,33]
list1=[]

for i in list:
    if i not in list1:
        list1.append(i)
print("given list:",list)
print("resultant list:",list1)



