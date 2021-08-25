#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 9, 2020
#This program prints: Shift Message by 1

mess= input('Please ennter a message: ')
print(mess)
for c in mess:

 print(c, (ord(c)+1),chr(ord(c)+1))
