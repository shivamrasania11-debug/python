def count(n):
    list=[]
    for i in range(n):
        x=int(input("enter elements:"))
        list.append(x)
    return list

n=int(input("enter n:"))
list1=count(n)
even=[]
odd=[]
for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("odd list elements:",odd)
print("even list elements:",even)
