#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 23, 2020
#This program prints: University Logo

import matplotlib.pyplot as plt #import libraries for plotting
import numpy as np #and for arrays (to hold images)
logoImg = np.ones((30,30,3)) #10x10 array with 3 sheets of 1’s

logoImg[:,:11,0:2] = 0

logoImg[:,-11:,0:2] = 0

logoImg[-11:,:,0:2] = 0
