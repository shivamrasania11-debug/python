def count(n):
    list=[]
    for i in range(n):
        x=int(input("enter elements:"))
        list.append(x)
    return list

n=int(input("enter the number:"))
list1=count(n)
y=int(input("enter the number you want to count:"))
print("given list:",list1)
print(f"total occurrences of {y} is {list1.count(y)}")

