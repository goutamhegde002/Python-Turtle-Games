import turtle

# Set up the screen
win = turtle.Screen()
win.title("Turtle Maze Runner")
win.bgcolor("lightblue")
win.setup(width=600, height=600)

# Create the turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(-250, 250)

# Create the goal
goal = turtle.Turtle()
goal.shape("circle")
goal.color("red")
goal.penup()
goal.goto(250, -250)

# Define the maze walls
walls = [
    (-300, 200, 600, 20),  # top wall
    (-300, -200, 600, 20), # bottom wall
    (-300, 200, 20, 400),  # left wall
    (280, 200, 20, 400),   # right wall
    (-150, 100, 300, 20),  # horizontal wall
    (100, -100, 300, 20)   # another horizontal wall
]

def create_wall(x, y, width, height):
    wall = turtle.Turtle()
    wall.shape("square")
    wall.color("black")
    wall.shapesize(stretch_wid=height/20, stretch_len=width/20)
    wall.penup()
    wall.goto(x, y)
    return wall

for wall in walls:
    create_wall(*wall)

# Functions to control the turtle
def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

# Check if the player has reached the goal
def check_goal():
    if player.distance(goal) < 20:
        print("You win!")
        player.goto(-250, 250)  # Reset the player position
    win.ontimer(check_goal, 100)

# Start the game
def start_game():
    # Hide the player and goal initially
    player.hideturtle()
    goal.hideturtle()

    # Display a start message
    start_message = turtle.Turtle()
    start_message.color("blue")
    start_message.penup()
    start_message.hideturtle()
    start_message.goto(0, 0)
    start_message.write("Press 'Space' to Start the Game", align="center", font=("Arial", 16, "bold"))

    def begin():
        start_message.clear()
        player.showturtle()
        goal.showturtle()
        check_goal()

    win.onkey(begin, "space")

# Keyboard bindings
win.listen()
win.onkey(move_up, "w")
win.onkey(move_down, "s")
win.onkey(move_left, "a")
win.onkey(move_right, "d")

# Start the game loop
start_game()
win.mainloop()
