num = int ( input ("Enter the limit.\n"))
i = 0
first_term = 0
second_term = 1
while (i<num):
    if(i<=1):
        next = i
    else:
        next=first_term+second_term
        first_term=second_term
        second_term=next
    print(next)
    i=i+1