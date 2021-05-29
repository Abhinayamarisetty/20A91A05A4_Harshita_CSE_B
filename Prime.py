#prime or not
n=int(input("Enter number"))
i=1
count=0
while(i<=n):
    if(n%i==0):
        count+=1
    i+=1
if (count==2):
    print("%d is a prime number" %(n))
else:
    print("%d is not a prime number" %(n))

OUTPUT:
Enter number23
23 is a prime number

Enter number26
26 is not a prime number
    
