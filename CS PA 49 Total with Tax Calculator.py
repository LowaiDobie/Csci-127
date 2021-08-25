#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: November 11, 2020
#This program prints: Total with Tax Calculator
print("------------------------------------------")
print("Welcome to the total with tax calculator!")
print("------------------------------------------")
print("Please enter the price of each item you would like to purchase, one at a time.")
print("Enter a negative number when you are done.")
price=float(input("Enter the price of an item: "))
total = price
tax = 0.0875
while price > 0:
    price= float(input("Enter the price of an item: "))
    total= total + price
    if price < 0:
        total = total- price
total = total + (total*tax)
print(total)
