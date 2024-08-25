import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Race")

# Define a list of colors and turtle names
colors = ["red", "blue", "green", "yellow", "purple"]
turtles = []

# Create turtles
for color in colors:
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.penup()
    racer.goto(-200, 100 - colors.index(color) * 50)
    turtles.append(racer)

# Draw the finish line
finish_line = turtle.Turtle()
finish_line.speed(0)
finish_line.penup()
finish_line.goto(200, 150)
finish_line.pendown()
finish_line.goto(200, -150)
finish_line.hideturtle()

# Start the race
race_on = True
while race_on:
    for racer in turtles:
        distance = random.randint(1, 5)
        racer.forward(distance)

        if racer.xcor() >= 200:
            print(f"{racer.color()[0].title()} turtle wins the race!")
            race_on = False
            break

screen.exitonclick()
