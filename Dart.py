import turtle
import random

# Set up the screen
win = turtle.Screen()
win.title("Turtle Darts Game")
win.bgcolor("lightblue")

# Create the dartboard
dartboard = turtle.Turtle()
dartboard.shape("circle")
dartboard.color("red")
dartboard.shapesize(10)
dartboard.penup()
dartboard.goto(0, 0)

# Create the dart
dart = turtle.Turtle()
dart.shape("triangle")
dart.color("black")
dart.penup()

score = 0

# Function to throw the dart
def throw_dart(x, y):
    global score
    dart.goto(x, y)
    distance = dart.distance(0, 0)
    if distance < 100:
        score += int((100 - distance) / 10)
    else:
        score -= 5
    print(f"Score: {score}")

# Start the game
win.onclick(throw_dart)
win.mainloop()
