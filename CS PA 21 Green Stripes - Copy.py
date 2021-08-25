#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 7, 2020
#This program prints: Green Stripes

import matplotlib.pyplot as plt #import libraries for plotting
import numpy as np #and for arrays (to hold images)
size = int(input("Enter the size: "))
output_file = input("Enter output file: ")

img = np.ones( (size,size,3) )
img[::2,:,0] = 0
img[::2,:,2] = 0

plt.imsave(output_file,img)
