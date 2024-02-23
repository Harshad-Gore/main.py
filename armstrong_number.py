#cheak whether entered number is arm strong or not
a = int (input("Enter an integer.\n"))
b = a
res = 0
while (b!=0):
    re = b % 10
    res = res + (re * re * re)
    b = b // 10
if (res == a):
    print(a,"is an ARMSTRONG number.")
else:
    print(a,"is not an ARMSTRONG number.")