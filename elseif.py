num=int(input("Enter number"))
if (num%2!=0)and(num<=20):
    print("Weird")
elif (2<=num<=5):
    print("Not weird")
elif (6<=num<=20):
    print("Weird")
else:
    print("Not weird")

OUTPUT:
Enter number1
Weird

Enter number4
Not weird

Enter number15
Weird

Enter number36
Not weird
