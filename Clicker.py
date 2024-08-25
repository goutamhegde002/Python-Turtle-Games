import turtle
import random
import time

# Set up the screen
win = turtle.Screen()
win.title("Turtle Clicker Game")
win.bgcolor("lightblue")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)

# Initialize variables
score = 0
high_score = 0
time_limit = 60
turtles_to_click = 100
level = 1

# Function to move the turtle to a random position
def move_turtle(x, y):
    global score
    t.hideturtle()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.showturtle()
    score += 1
    print(f"Score: {score}")

# Function to start the game
def start_game():
    global score, level, time_limit, turtles_to_click, high_score
    
    for level in range(1, 4):
        # Adjust game parameters based on the level
        if level == 2:
            time_limit = 30
            turtles_to_click = 100
        elif level == 3:
            time_limit = 15
            turtles_to_click = 50

        # Reset score for the new level
        score = 0
        print(f"Level {level} - You have {time_limit} seconds to click {turtles_to_click} turtles!")

        # Start the timer
        start_time = time.time()

        while time.time() - start_time < time_limit and score < turtles_to_click:
            t.onclick(move_turtle)
            win.update()

        # Check if the player has completed the level
        if score >= turtles_to_click:
            print(f"Level {level} complete! Moving to the next level.")
        else:
            print(f"Level {level} failed! Your final score: {score}")
            break

        # Update high score if the current score is higher
        if score > high_score:
            high_score = score

    print(f"Game over! Your highest score: {high_score}")

# Start the game
start_game()

# Keep the window open
win.mainloop()
