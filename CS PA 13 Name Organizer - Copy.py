#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 16, 2020
#This program prints: Name Organizer

mess= input()
newnames = mess.split('; ')

for mess in newnames:
        str = mess.split(",")
        print(str[1][1]+".",str[0])

