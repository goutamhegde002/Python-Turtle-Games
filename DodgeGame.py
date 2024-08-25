import turtle
import random

win = turtle.Screen()
win.title("Turtle Dodge Game")
win.bgcolor("lightgray")
win.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(0, -250)

# Create the falling obstacle
obstacle = turtle.Turtle()
obstacle.shape("circle")
obstacle.color("red")
obstacle.penup()
obstacle.speed(0)
obstacle.goto(random.randint(-280, 280), 250)

score = 0

# Function to move the player left and right
def move_left():
    x = player.xcor()
    x -= 20
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 280:
        x = 280
    player.setx(x)

# Function to drop the obstacle
def drop_obstacle():
    global score
    y = obstacle.ycor()
    y -= 20
    obstacle.sety(y)

    if obstacle.ycor() < -300:
        obstacle.goto(random.randint(-280, 280), 250)
        score += 1
        print(f"Score: {score}")

    if player.distance(obstacle) < 20:
        print(f"Game Over! Final Score: {score}")
        win.bye()

    win.ontimer(drop_obstacle, 100)

# Keyboard bindings
win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")

# Start dropping obstacles
drop_obstacle()

win.mainloop()
