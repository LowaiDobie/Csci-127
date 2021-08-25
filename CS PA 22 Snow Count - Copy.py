#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 7, 2020
#This program prints: Snow Count 

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

newimg=input()
ca = plt.imread(newimg)   #Read in image
countSnow = 0            #Number of pixels that are almost white
t = 0.8                 #Threshold for almost white-- can adjust between 0.0 and 1.0

#For every pixel:
for row in range(ca.shape[0]):
     for col in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[row,col,0] > t) and (ca[row,col,1] > t) and (ca[row,col,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)
