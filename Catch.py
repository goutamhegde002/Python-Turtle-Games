import turtle
import random
import time

win = turtle.Screen()
win.title("Turtle Catch Game")
win.bgcolor("lightyellow")
win.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(0, -250)

# Create the falling object
falling_object = turtle.Turtle()
falling_object.shape("circle")
falling_object.color("red")
falling_object.penup()
falling_object.speed(0)
falling_object.goto(random.randint(-280, 280), 250)

score = 0
lives = 3

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

# Function to drop the object
def drop_object():
    global score, lives
    y = falling_object.ycor()
    y -= 20
    falling_object.sety(y)

    if falling_object.ycor() < -300:
        falling_object.goto(random.randint(-280, 280), 250)
        lives -= 1
        if lives == 0:
            print(f"Game Over! Final Score: {score}")
            win.bye()

    if player.distance(falling_object) < 20:
        score += 10
        print(f"Score: {score}")
        falling_object.goto(random.randint(-280, 280), 250)

    win.ontimer(drop_object, 100)

# Keyboard bindings
win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")

# Start dropping objects
drop_object()

win.mainloop()
