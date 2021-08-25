#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 21, 2020
#This program prints: Turtle string
import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == 'B':          #turn right
        tess.backward(50)
    elif ch == 'D':          #turn right
        tess.dot()
    elif ch == 'S':          #turn right
        tess.stamp()
    elif ch == 'p':          #turn right
        tess.color("purple")
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'r':          #turn red
        tess.color("red")
    elif ch == 'g':          #turn green
        tess.color("green")
    elif ch == 'b':          #turn blue
        tess.color("blue")
    else:                    #for any other character, print an error message
        print("Error: do not know the command:", ch)

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked
