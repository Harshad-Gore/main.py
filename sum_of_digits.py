#display sum of all digits of entered number.
a = (input("Enter an integer.\n"))
res = 0
for i in range (0,len(a)):
    res = (res + int(a[i]))
print("Sum of digits is :",res)