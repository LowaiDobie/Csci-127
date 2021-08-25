#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 15, 2020
#This program prints: Shelter Census
import matplotlib.pyplot as plt
import pandas as pd
fil=input("Enter name of input file: ")
out=input("Enter name of output file: ")
shel=pd.read_csv(fil)
shel['Fraction Single Women']=shel['Single Adult Women in Shelter']/shel['Total Individuals in Shelter']
shel.plot(x='Date of Census', y='Fraction Single Women')
fig = plt.gcf()
fig.savefig(out)
