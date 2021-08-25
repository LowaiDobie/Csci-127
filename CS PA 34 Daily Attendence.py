#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 21, 2020
#This program prints: Daily Attendence 
import matplotlib.pyplot as plt
import pandas as pd
fil=input("Enter name of input file: ")
out=input("Enter name of output file: ")
df=pd.read_csv(fil)
df["Date"] = pd.to_datetime(df["Date"].apply(str))
df['% Attending']= (df['Present']/df['Enrolled'])*100
df.plot(x='Date',y='% Attending')
fig = plt.gcf()
fig.savefig(out)
