a=[]
fact=[]
ch="y"
while (ch=="y") or(ch=="Y"):
    item=int(input("Enter the list of numbers you want to factorise.\n"))
    a.append(item)
    ch=input("Do you want to insert more numbers.(Y/n)\n")
print("The list is",a)
for i in a:
    f=1
    for j in range(1,i+1):
        f=f*j
    fact.append(f)
print("The factorial of each element is :",fact)