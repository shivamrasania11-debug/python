'''
A
A B
A B C
A B C D
'''

n=int(input("enter n:"))

for i in range(1, n+1):
    ch=65
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print()
    
        
