#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 23, 2020
#This program prints: Number of Coins
cents=int(input("Enter the number of cents: "))
quarters = cents // 25
cents %= 25
dimes = cents // 10
cents %= 10
nickels = cents // 5
cents %= 5
pennies = cents

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Cents:", cents)
