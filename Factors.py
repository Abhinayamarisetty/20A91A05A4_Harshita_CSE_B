#factors of given number
n=int(input("Enter number"))
i=1
print("The factors of %d is" %(n))
while (i<=n):
    if (n%i==0):
        print(i)
    i+=1

OUTPUT:
Enter number8
The factors of 8 is
1
2
4
8
