#Write a Python program to check whether a String is Palindrome or not.
#Hint: Palindrome means original string and its reverse both are same.

n=input("enter the string:")

rev=n[::-1]

if rev == n:
    print("string is palindrome")
else:
    print("string is not palindrome")
