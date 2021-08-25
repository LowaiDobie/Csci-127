#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: September 5, 2020
#This program prints: HotPink Screen

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("hotpink")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("black")
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("lightgreen")

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin

alex.forward(50)                 # make alex draw a square
alex.left(72)
alex.forward(50)
alex.left(72)
alex.forward(50)
alex.left(72)
alex.forward(50)
alex.left(72)
alex.forward(50)
alex.left(72)

wn.exitonclick()
