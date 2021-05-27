start=int(input("Enter the start value"))
end=int(input("Enter the end value"))
count=int(input("Enter the step count"))
while(start<=end):
    print(start)
    start=start+count
print("After while loop the value of i is",format(start))
print("After while loop the value %d belongs to i" %(start))
    
OUTPUT:
Enter the start value2
Enter the end value16
Enter the step count4
2
6
10
14
After while loop the value of i is 18
After while loop the value 18 belongs to i

