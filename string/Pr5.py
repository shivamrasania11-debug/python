#Write a Python function that accepts a string and count the number of
#upper, lower case letters, digits and other characters.


def countval(str):
 
    upper=0
    lower=0
    digit=0
    special=0

    for char in str:
        if char.isupper():
            upper=upper+1
        elif char.islower():
            lower=lower+1
        elif char.isdigit():
            digit=digit+1
        else:
            special=special+1
        

    print("upper case characters:",upper)
    print("lower case characters:",lower)

    print("digit in string:",digit)

    print("special characters is:",special)

str=input("enter the string:")
countval(str)
