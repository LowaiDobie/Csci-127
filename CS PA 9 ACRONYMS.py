#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 9, 2020
#This program prints: Acronyms

mess= input("enter a prhase: ")
print("Your phrase in capital letters: ",mess.upper())
mess_split= mess.split()
acronym=""
for i in (mess_split):
    acronym=(acronym+i[0].upper())
print(acronym)






