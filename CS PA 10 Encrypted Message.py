#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 9, 2020
#This program prints: Encrypted Message

word= input("Enter word here: ")
newword=""
for i in word:
    Offset=ord(i)-ord('A')+13
    warp= Offset % 26
    newchr=chr(ord('A')+warp)
    newword= newword + newchr

print("Your word in code is: ", newword.upper())
