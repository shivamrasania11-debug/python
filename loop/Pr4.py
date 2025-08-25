n=int(input("enter the number:"))

if n <= 1:
    print("number is not prime")
elif n==2 or n==3 or n==5 or n==7:
    print("number is prime")
elif n % 2==0 or n%3==0 or n%5==0 or n%7==0:
    print("number is not prime")
else:
    print("number is prime")
