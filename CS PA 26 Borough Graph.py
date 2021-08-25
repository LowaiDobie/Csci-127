#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 15, 2020
#This program prints: Borough Graph
import matplotlib.pyplot as plt
import pandas as pd
bor1=input("Enter first borough name: ")
bor2=input("Enter second borough name: ")
out=input("Enter output file name: ")
#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = (pop[bor1] + pop[bor2]) / pop['Total']
pop.plot(x = 'Year', y = 'Fraction')


#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(out)
