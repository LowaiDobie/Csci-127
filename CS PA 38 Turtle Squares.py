#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 28, 2020
#This program prints: Turtle Squares
import turtle

def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist, 
    to move the turtle and a color, col, to set the turtle's color.
    """
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def squares(t, length):
    if length > 10:
        for i in range (4):
            t.forward(length)
            t.left(90)
        squares(t, length/2)
            


def nestedSquares(t, length):
  if length > 10:
        for i in range (4):
            t.forward(length)
            t.left(90)
            nestedSquares(t, length/2)
            
def main():
    n = int(input('Enter edge length: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    squares(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedSquares(tess, n)

if __name__ == "__main__":
     main()
