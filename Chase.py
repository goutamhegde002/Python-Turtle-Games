import turtle
import random

# Set up the screen
win = turtle.Screen()
win.title("Turtle Chase Game")
win.bgcolor("lightblue")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)

score = 0
speed = 1

# Function to move the turtle to a random position
def move_turtle(x, y):  # Accepting x, y parameters
    global score, speed
    t.hideturtle()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.showturtle()
    score += 1
    speed += 1
    t.speed(speed)
    print(f"Score: {score}")

# Function to start the game
def start_game():
    t.onclick(move_turtle)

start_game()
win.mainloop()
