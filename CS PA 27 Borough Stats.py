#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 15, 2020
#This program prints: Borough Stats
import matplotlib.pyplot as plt
import pandas as pd
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
bor1=input("Enter first borough name: ")
print("Min: ",pop[bor1].min())
print("Max: ",pop[bor1].max())
print("Mean: ",pop[bor1].mean())
print("Median: ",pop[bor1].median())
print("Standard Deviation: ",pop[bor1].std())
