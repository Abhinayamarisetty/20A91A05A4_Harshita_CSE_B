amount=int(input("Enter amount"))
if amount<1000:
    print("Total bill is",amount)
elif (1000<=amount<2000):
    print("Total bill is",amount)
    print("Discount on the billed amount is 100")
    discount=amount-100
    print("Paid bill is",discount)
elif (2000<=amount<3000):
    print("Total bill is",amount)
    print("Discount on the billed amount is 400")
    discount=amount-400
    print("Paid bill is",discount)
elif (3000<=amount<5000):
    print("Total bill is",amount)
    print("Discount on the billed amount is 900")
    discount=amount-900
    print("Paid bill is",discount)
else:
    print("Total bill is",amount)
    print("Discount on the billed amount is 2000")
    discount=amount-2000
    print("Paid bill is",discount)

OUTPUT:
Enter amount900
Total bill is 900

Enter amount1600
Total bill is 1600
Discount on the billed amount is 100
Paid bill is 1500

Enter amount2500
Total bill is 2500
Discount on the billed amount is 400
Paid bill is 2100

Enter amount3700
Total bill is 3700
Discount on the billed amount is 900
Paid bill is 2800

Enter amount5800
Total bill is 5800
Discount on the billed amount is 2000
Paid bill is 3800

