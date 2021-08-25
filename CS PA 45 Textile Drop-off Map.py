#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: November 4, 2020
#This program prints: Textile Drop-off Map
import folium
import pandas as pd
fil=input("Please enter the name of the input file: ")
out_file=input("Please enter the name of the output file: ")
bor=input("Please enter the name of the borough: ")
df=pd.read_csv(fil)
dfCopy = df.groupby("Borough").get_group(bor)
mapCUNY = folium.Map(location=[40.768731, -73.964915])
for index,row in dfCopy.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Address"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)
mapCUNY.save(outfile=out_file)
