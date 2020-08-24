# use arrow keys to control, press q to quit

# Turtle Graphics Game
import turtle
import math
import random

# loop status
state = True

# Set up screen
wn = turtle.Screen()
wn.bgcolor("green")

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)


# Set speed variable
speed = 1


# Define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

def exit():
    global state
    state = False
    wn.bye()


def out_of_bounds(x, y):
    if x > 300 or x < -300:
        player.right(180)

    if y > 300 or y < -300:
        player.right(180)



# Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")
turtle.onkey(exit, "q")

while state:
    player.forward(speed)
    # Boundary Checking
    out_of_bounds(player.ycor(),player.xcor())

