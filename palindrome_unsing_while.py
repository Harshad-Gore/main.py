num =int(input("Enter a positive integer.\n"))
x=num
r=0
while (num>0):
    d=num%10
    r=r*10+d
    num=num//10
if x==r:
    print("The number is palindrome.\n")
else:
    print("The number is not a palindrome.\n")