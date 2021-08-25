#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 16, 2020
#This program prints: Shades of Blue

import turtle				

turtle.colormode(255)		
tess = turtle.Turtle()		
tess.shape("turtle")		
tess.backward(100)			 

for i in range(0,255,10):
     tess.forward(10)		
     tess.pensize(i)		
     tess.color(0,0,i)		
for i in range(255,0,-10):
     tess.forward(10)		
     tess.pensize(i)		
     tess.color(0,0,i)		
