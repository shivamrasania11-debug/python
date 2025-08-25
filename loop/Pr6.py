n=int(input("enter the number:"))

r=0
rev=0
print("original number:",n)
while n!=0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print("reverse number:",rev)    
    
