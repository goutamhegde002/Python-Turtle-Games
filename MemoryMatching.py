import turtle
import random
import time

# Set up the screen
win = turtle.Screen()
win.title("Memory Matching Game")
win.bgcolor("lightblue")
win.setup(width=600, height=600)

# Memory game cards
symbols = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼'] * 2
random.shuffle(symbols)

tiles = []
revealed = []

# Create tiles for the game
for i in range(4):
    row = []
    for j in range(4):
        tile = turtle.Turtle()
        tile.shape("square")
        tile.color("black")
        tile.penup()
        tile.goto(-150 + j * 100, 150 - i * 100)
        tile.symbol = symbols.pop()
        tile.revealed = False
        row.append(tile)
    tiles.append(row)

moves = 0
matched_pairs = 0

def reveal_tile(tile):
    global moves, matched_pairs

    if tile.revealed:
        return

    tile.write(tile.symbol, align="center", font=("Arial", 24, "normal"))
    tile.revealed = True
    revealed.append(tile)

    if len(revealed) == 2:
        win.update()
        time.sleep(1)

        if revealed[0].symbol == revealed[1].symbol:
            matched_pairs += 1
        else:
            for t in revealed:
                t.clear()
                t.revealed = False

        revealed.clear()
        moves += 1

    if matched_pairs == 8:
        print(f"Game over! Total moves: {moves}")

def setup_bindings():
    for row in tiles:
        for tile in row:
            win.onclick(lambda x, y, tile=tile: reveal_tile(tile), 1, True)

setup_bindings()

# Keep the window open
win.mainloop()
