n = int(input("Enter an integer.\n"))
x=n
r=0
while (n>0):
    d = n%10
    r = r*10 +d
    n = n//10
print("The reverse of integer is :",r)