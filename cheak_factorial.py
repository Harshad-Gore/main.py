a=int(input("Enter the number.\n"))
factorial = 1
if (a<0):
    print("Factorial of negative number does not exist.\n")
elif(a==0):
    print("Factorial of 0 is 1.\n")
else:
    for i in range(1,a+1):
        factorial = factorial * i
print("The factorial of",a,"is",factorial)