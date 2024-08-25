import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Rangoli Making Game")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed
pen.width(2)

# Colors list
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]

# Function to draw a circle pattern
def draw_circle(radius, color):
    pen.color(color)
    pen.circle(radius)

# Function to draw a rangoli pattern
def draw_rangoli(size):
    for i in range(12):  # 12 patterns in a circle
        draw_circle(size, random.choice(colors))
        pen.right(30)  # Turn the pen to create circular patterns

# Function to start the game
def start_game():
    pen.penup()
    pen.goto(0, -150)  # Starting point
    pen.pendown()

    # Draw multiple rangolis with increasing size
    for size in range(50, 150, 20):
        draw_rangoli(size)

    pen.penup()
    pen.goto(0, 0)
    pen.hideturtle()
    screen.exitonclick()  # Exit on click

# Start the game
start_game()
