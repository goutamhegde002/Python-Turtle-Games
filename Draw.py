import turtle
import random

# Set up the screen
win = turtle.Screen()
win.title("Turtle Drawing Game")
win.bgcolor("white")

# Create a turtle
draw_turtle = turtle.Turtle()
draw_turtle.shape("turtle")
draw_turtle.color("black")
draw_turtle.speed(1)

# Functions to control the turtle
def move_up():
    draw_turtle.setheading(90)
    draw_turtle.forward(50)

def move_down():
    draw_turtle.setheading(270)
    draw_turtle.forward(50)

def move_left():
    draw_turtle.setheading(180)
    draw_turtle.forward(50)

def move_right():
    draw_turtle.setheading(0)
    draw_turtle.forward(50)

def change_color():
    colors = ["red", "green", "blue", "yellow", "purple"]
    draw_turtle.color(random.choice(colors))

def pen_up():
    draw_turtle.penup()

def pen_down():
    draw_turtle.pendown()

# Keyboard bindings
win.listen()
win.onkey(move_up, "Up")
win.onkey(move_down, "Down")
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")
win.onkey(change_color, "space")
win.onkey(pen_up, "u")
win.onkey(pen_down, "d")

# Keep the window open
win.mainloop()
