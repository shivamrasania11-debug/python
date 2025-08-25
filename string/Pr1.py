#Write a Menu driven program for string operations(upper, lower, reverse
#and length):

def menu():
    print("String Operations")
    print("1.upper")
    print("2.lower")
    print("3.reverse")
    print("4.length")
    print("5.exit")
    ch=int(input("enter your choice:"))
    return ch

while True:
        ch=menu()
        if ch==5  :
            break
        str=input("enter the string:")
        if ch==1:
            print("upper case string is:",str.upper())
            break
        if ch==2:
            print("lower case string is:",str.lower())
            break
        if ch==3:
            print("reverse string is:",str[::-1])
            break
        if ch==4:
            print("length of string is:",len(str))
            break
        input()
    
 
