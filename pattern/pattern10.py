'''
    A
   AB
  ABC
 ABCD

'''

n=int(input("enter n:"))

for i in range(1,n+1):
    ch=65
    for k in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print()
