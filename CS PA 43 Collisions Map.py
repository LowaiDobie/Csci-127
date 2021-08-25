#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: November 4, 2020
#This program prints: Collisions Map
import folium
import pandas as pd
fileName=input("Enter CSV file name: ")
out_file=input("Enter output file: ")
df=pd.read_csv(fileName)
mapCol = folium.Map(location=[40.768731, -73.964915])

for index,row in df.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCol)
mapCol.save(outfile=out_file)
