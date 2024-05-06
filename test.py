from tkinter import *
from functools import partial

# Initialize the main window
root = Tk()
root.title("Caro by SAM")

# Create a dictionary to hold buttons
Buts = {}
score = {'X': 0, 'O': 0}  # Initial score dictionary

# Function to handle button clicks
def xulynut(x, y):
    if Buts[x, y]['text'] == '':
        Buts[x, y]['text'] = 'X'  # Assuming 'X' is the current player
        update_scoreboard()

def update_scoreboard():
    # This function updates the scoreboard; you might call it under certain conditions
    score_label.config(text=f"X: {score['X']}\nO: {score['O']}")

# Create main frames for the board and the scoreboard
board_frame = Frame(root)
board_frame.pack(side="left")

score_frame = Frame(root, width=200, height=400, bd=2, relief="ridge", padx=10, pady=10)
score_frame.pack(side="right", fill="both", expand=True)

# Scoreboard label
score_label = Label(score_frame, font=('arial', 14, 'bold'), text=f"X: {score['X']}\nO: {score['O']}")
score_label.pack(side="top", fill="x", expand=True)

# Create grid buttons
for r in range(15):
    for c in range(15):
        Buts[r, c] = Button(board_frame, font=('Helvetica', 15), bd=1, height=2, width=2,
                            borderwidth=0, command=partial(xulynut, x=r, y=c), highlightthickness=0)
        Buts[r, c].grid(row=r, column=c, sticky="nsew")

# Run the main event loop
root.mainloop()
