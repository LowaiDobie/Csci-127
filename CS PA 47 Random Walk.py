#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: November 11, 2020
#This program prints: Random Walk
import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(200):
  trey.forward(5)
  a = random.randrange(0,360,30)
  trey.right(a)
