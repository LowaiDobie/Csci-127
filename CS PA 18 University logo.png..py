#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 23, 2020
#This program prints: University Logo
import matplotlib.pyplot as plt
import numpy as np


logoImg = np.ones((30, 30, 3))


logoImg[:,:10,1] = 0
logoImg[:,:10,2] = 0


logoImg[:,-10:,1] = 0
logoImg[:,-10:,2] = 0

logoImg[-10:,:,1] = 0
logoImg[-10:,:,2] = 0


plt.show("logo.png",logoImg)
