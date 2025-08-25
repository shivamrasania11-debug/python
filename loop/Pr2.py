
n=int(input("enter the number:"))

n1=0
n2=1

for i in range(1,n+1):
    print(f"{n1}",end=" ")
    next=n1+n2
    n1=n2
    n2=next
    
