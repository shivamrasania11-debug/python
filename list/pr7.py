def count(n):
    list=[]
    for i in range(n):
        x=input("enter elements:")
        list.append(x)
    return list

n=int(input("enter n:"))
list1=count(n)
list2=[]
print("original list:",list1)
for v in list1:
    list2.append(v[0].upper())
print("output list:",list2)
    
