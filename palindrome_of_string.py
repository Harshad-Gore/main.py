#program to find the entered string is pallindrome or not
x = input("Enter a string.\n")
w=""
for i in x:
    w = i + w
    if (x==w):
        print("String is palindrome.")
if (x!=w):
    print("String is not palindrom.")