a=int(input("Enter a"))
b=int(input("Enter b"))
c=a**b
count=0
while(c!=0):
    r=c%10
    sum=r
    count+=1
    if(count==1):
        break
print("%d**%d is %d and last digit is %d" %(a,b,c,sum))

OUTPUT:
Enter a16
Enter b3
16**3 is 4096 and last digit is 6
