a = int(input("Enter the limit.\n"))
n = []
for i in range (1,a+1):
    a = int(input("Enter element.\n"))
    n.append(a)
print(n)
l = len(n)
for i in range(l):
    for j in range(0,l-i-1):
        if n[j]>n[j+1]:
            temp = n[j]
            n[j] = n[j+1]
            n[j+1] = temp
print("After sorting the list is")
print(n)