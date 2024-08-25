# -*- coding: utf-8 -*-
"""
@author: Goutam@002
"""
# Import the necessary libraries
import turtle as t
import random as rd

# Define a function to add a space background to the turtle screen
def add_space_background():
    # Create a turtle screen
    screen = t.Screen()
    # Set the background image to a space background
    screen.bgpic(r"C:\Users\User\Downloads\moon-2048727.png")

# Define a function to increase the size of the candy turtle
def increase_candy_size():
    # Create a candy turtle
    candy = t.Turtle()
    # Define the candy shape
    candy_shape =  ((0,0),(10,-2),(12,0),(10,2))
    # Set the turtle pen properties
    candy.pen(pensize=3)
    candy.shapesize(2,2)
    # Set the candy shape
    t.register_shape("candy", candy_shape)
    candy.shape("candy")
    return candy

# Call the add_space_background function to set the background image
add_space_background()

# Set the background color to black
t.bgcolor('black')

# Create a UFO turtle and set its properties
UFO = t.Turtle()
UFO_shape = ((0,0),(20,-5),(25,0),(20,5))
t.register_shape('UFO', UFO_shape)
UFO.shape('UFO')
UFO.color('red')
UFO.speed(0)
UFO.penup()
UFO.hideturtle()

# Call the increase_candy_size function to create a candy turtle and set its properties
candy = increase_candy_size()
candy.color('orange')
candy.penup()
candy.hideturtle()
candy.speed(0)

# Set the initial game state to not started
game_started = False

# Create a text turtle and display the game instructions
text_turtle = t.Turtle()
text_turtle.color('Red')
text_turtle.write('IGNITE THE UFO\n', align='center', font=('Arial', 50, 'bold'))
text_turtle.pensize(20)
text_turtle.color('black')
text_turtle.write('\nGet those candies\n', align='center', font=('Times New roman', 16, 'bold'))
text_turtle.color('black')
text_turtle.write('\nPress Space to start the game!', align='center', font=('Times New roman', 10, 'bold'))
text_turtle.hideturtle()

# Create a score turtle and set its properties
score_turtle = t.Turtle()
score_turtle.color('white')
score_turtle.hideturtle()
score_turtle.speed(0)

# Define a function to check if the UFO is outside the turtle screen
def outside_window():
    left_wall = -t.window_width()/2
    right_Wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = UFO.pos()
    outside = x < left_wall or x > right_Wall or y > top_wall or y < bottom_wall
    return outside

# Define a function to display the game over message and restart the game on space key press
def game_over():
    UFO.color('black')
    candy.color('black')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER !', align='center', font=('Arial', 30, 'normal') )
    t.onkey(start_game,'space')

# Define a function to display the current score on the score turtle
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 70
    y = (t.window_height()/2) - 70
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

# Define a function to place the candy turtle at a random position
def place_candy():
    candy.hideturtle()
    candy.setx(rd.randint(-200,200))
    candy.sety(rd.randint(-200,200))
    candy.showturtle()

# Define the main game function
def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    
    score = 0
    text_turtle.clear()

    UFO_speed = 1.25
    UFO_length = 3
    UFO.shapesize(1,UFO_length,1)
    UFO.showturtle()
    display_score(score)
    place_candy()

    # Loop until the UFO goes outside the turtle screen
    while True:
        UFO.forward(UFO_speed)
        if UFO.distance(candy) < 20:
            place_candy()
            UFO_length = UFO_length + 1
            UFO.shapesize(1,UFO_length,1)
            UFO_speed = UFO_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

# Define functions to move the UFO turtle in different directions and restart the game on up key press
def move_up():
    UFO.setheading(90)

def move_down():
        UFO.setheading(270)

def move_left():
        UFO.setheading(180)

def move_right():
        UFO.setheading(0)
        
def restart_game():
 start_game()

# Set up key bindings for starting and restarting the game and moving the UFO turtle
t.onkey(start_game,'space')
t.onkey(restart_game,'Up')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()