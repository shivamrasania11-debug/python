n=int(input("enter n:"))

for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print(j,end=" ")
    print()
