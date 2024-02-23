a=int(input("Enter number.\n"))
rem =a%2
if (a==0) or (a<0):
    print("You entered a number 0 or less than 0.")
elif rem == 0:
    print(a,"is a even number.")
else:
    print(a,"is not a even number.")