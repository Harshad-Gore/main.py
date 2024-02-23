num=int(input("Enter the number of rows.\n"))
for i in range (num):
    for j in range (i+1):
        print("*",end="")
    print("")