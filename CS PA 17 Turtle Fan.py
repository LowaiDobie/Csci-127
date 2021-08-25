#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 23, 2020
#This program prints: Turtle Fan

import turtle
alex = turtle.Turtle()

stamp= int(input("Enter number of stamps the turtle will print: "))

alex.shape("circle")
alex.penup()
steps=20

for i in range(stamp):
    alex.stamp()
    if i % 4 == 0:
        steps=steps+2
    alex.forward(steps)
    alex.right(24)
