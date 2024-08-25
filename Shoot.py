import turtle
import random

# Set up the screen
win = turtle.Screen()
win.title("Turtle Shooting Game")
win.bgcolor("lightblue")

# Create the shooter turtle
shooter = turtle.Turtle()
shooter.shape("triangle")
shooter.color("black")
shooter.penup()
shooter.goto(0, -250)
shooter.setheading(90)

# Create the target
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.goto(0, 250)

# Function to fire the bullet
def fire_bullet():
    bullet = turtle.Turtle()
    bullet.shape("circle")
    bullet.color("yellow")
    bullet.penup()
    bullet.goto(shooter.xcor(), shooter.ycor())
    bullet.setheading(90)
    bullet.speed(1)

    while bullet.ycor() < 300:
        bullet.forward(10)
        if bullet.distance(target) < 20:
            print("Hit!")
            target.goto(random.randint(-200, 200), random.randint(0, 250))
            bullet.hideturtle()
            break

# Keyboard binding
win.listen()
win.onkey(fire_bullet, "space")

win.mainloop()
