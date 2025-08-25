def count(n):
    list=[]
    for i in range(n):
        x=int(input("enter elements:"))
        list.append(x)
    return list
n=int(input("enter the number:"))
list1=count(n)
print("given list:",list1)
print("smallest number:",min(list1))
print("largest number:",max(list1))
