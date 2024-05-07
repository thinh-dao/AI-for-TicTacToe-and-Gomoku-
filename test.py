import tkinter as tk
from tkinter import *
from functools import partial
import time

# Initialize the main window
root = Tk()
root.title("Gomoku")

# Create a dictionary to hold buttons
Buts = {}
score = {'X': 0, 'O': 0}  # Initial score dictionary
current_turn = 'X'  # Start game with player X

# Function to handle button clicks
def xulynut(x, y):
    global current_turn
    if Buts[x, y]['text'] == '':
        Buts[x, y]['text'] = current_turn  # Place current player's mark
        update_scoreboard()
        update_turn()  # Update whose turn it is

def update_turn():
    global current_turn
    current_turn = 'O' if current_turn == 'X' else 'X'
    turn_label.config(text=f"It is {current_turn}'s turn")

def update_scoreboard():
    # This function updates the scoreboard; you might call it under certain conditions
    score_label.config(text=f"Player X: {score['X']}\n\nPlayer O: {score['O']}")

# Scoreboard frame setup
score_frame = Frame(root, bd=3, relief="groove", padx=10, pady=10)
score_frame.pack(side="right", fill="both", expand=True)

# Scoreboard title label
scoreboard_title = Label(score_frame, font=('Segoe UI', 25, 'bold'), text="Scoreboard", anchor=tk.CENTER)
scoreboard_title.pack(side="top", fill="x")

# Scoreboard label
score_label = Label(score_frame, font=('Segoe UI', 20), anchor=tk.CENTER, justify=tk.LEFT)
score_label.pack(side="top", fill="x", expand=True)

# Turn label above the board frame
turn_label = Label(root, text=f"It is {current_turn}'s turn", font=('Segoe UI', 20, 'bold'), pady=5)
turn_label.pack()

# Board frame setup
board_frame = Frame(root)
board_frame.pack(side="left")

# Initially update scoreboard to display initial scores
update_scoreboard()

# Create grid buttons
for r in range(15):
    board_frame.rowconfigure(r, weight=1, minsize=2, pad=0)
    board_frame.columnconfigure(r, weight=1, minsize=2, pad=0)
    for c in range(15):
        Buts[r, c] = Button(board_frame, font=('Segoe UI', 18), height=2, width=2,
                            borderwidth=0, command=partial(xulynut, x=r, y=c), highlightthickness=0)
        Buts[r, c].grid(row=r, column=c, sticky="nsew")

# Run the main event loop
root.mainloop()
