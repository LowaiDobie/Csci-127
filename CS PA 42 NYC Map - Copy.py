#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: November 4, 2020
#This program prints: NYC Map
import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

P=folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)
mapCUNY.save(outfile='nycMap.html')
