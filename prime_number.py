num = int (input("Enter number.\n"))
lim=int(num/2)+1
for i in range(2,lim):
    rem=num%i
    if rem == 0:
        print(num,"is not a prime number.")
        break
else:
    print(num,"is a prime number.")