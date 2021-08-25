#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 23, 2020
#This program prints: Seconds to time 

time = float(input("Please enter time in seconds: "))
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("%dh: %dm: %ds" %(hour, minutes, seconds))
