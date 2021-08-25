#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 21, 2020
#This program prints: Air Pollution
import matplotlib.pyplot as plt
import pandas as pd
fil=input("Enter name of input file: ")
out=input("Enter name of output file: ")
aqu=pd.read_csv(fil)
avg=aqu.groupby('geo_entity_name').mean()['data_valuemessage']
avg.plot.bar()
plt.gcf().subplots_adjust(bottom=0.5) 
fig = plt.gcf()
fig.savefig(out)
