#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 15, 2020
#This program prints: Stars Data
import pandas as pd

fil=input("Enter file name: ")
col=input("Enter the name of the column: ")
pop = pd.read_csv(fil)

print("The average",col,"for each Star type is: ")
avg = pop.groupby('Star type').mean()
print(avg[col])
