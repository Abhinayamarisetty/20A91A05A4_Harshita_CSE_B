amount=int(input("Enter amount"))
if amount<1000:
    print("Total bill is",amount)
elif (1000<=amount<2000):
    print("Total bill is",amount)
    discount=(amount)*(10/100)
    print("Discount on the billed amount is",discount)
    print("Paid bill is",amount-discount)
elif (2000<=amount<3000):
    print("Total bill is",amount)
    discount=(amount)*(20/100)
    print("Discount on the billed amount is",discount)
    print("Paid bill is",amount-discount)
elif (3000<=amount<5000):
    print("Total bill is",amount)
    discount=(amount)*(30/100)
    print("Discount on the billed amount is",discount)
    print("Paid bill is",amount-discount)
else:
    print("Total bill is",amount)
    discount=(amount)*(40/100)
    print("Discount on the billed amount is",discount)
    print("Paid bill is",amount-discount)

OUTPUT:
Enter amount900
Total bill is 900

Enter amount1600
Total bill is 1600
Discount on the billed amount is 160.0
Paid bill is 1440.0

Enter amount2700
Total bill is 2700
Discount on the billed amount is 540.0
Paid bill is 2160.0

Enter amount3800
Total bill is 3800
Discount on the billed amount is 1140.0
Paid bill is 2660.0

Enter amount5900
Total bill is 5900
Discount on the billed amount is 2360.0
Paid bill is 3540.0


