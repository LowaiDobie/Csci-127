#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 28, 2020
#This program prints: Film Permits
import matplotlib.pyplot as plt
import pandas as pd
fileName=input("Enter file name: ")
df=pd.read_csv(fileName)
num=df["EventType"].count()
print("There were",num,"film permits")
print(df['Borough'].value_counts())
print()
print()
print("The three most popular type of events were:")
print(df['EventType'].value_counts()[:3])
