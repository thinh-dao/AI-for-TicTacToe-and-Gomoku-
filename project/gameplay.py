"""
This module contains the GamePlay class which is responsible for running the game between two players.
!The code should not be modified.
"""
import time
from .player import Player
from .game import Game

class GamePlay():
    def __init__(self, x_player: Player, o_player: Player, game: Game , mode: str = "plain"):
        """
        Three modes for visualization of the game:
        1. "silent": game play is not shown (Not available for Human Player)
        2. "plain": game play is shown in terminal
        3. "ui": game play is shown with GUI       
        """
        self.x_player = x_player
        self.o_player = o_player
        self.mode = 'plain'
        
        # Check player initialization
        assert (self.x_player.letter == 'X'), "Wrong letter initialization for Player 1!"
        assert (self.o_player.letter == 'O'), "Wrong letter initialization for Player 2"
        
        self.game = game
        
    def run(self, print_game=True):
        if print_game:
            self.game.init_board()

        current_turn = 'X'
        winner = None
        
        while len(self.game.avail_moves) > 0:
            if current_turn == 'X':
                curr_player = self.x_player
            else:
                curr_player = self.o_player
                
            move = curr_player.get_move(self.game)
            x, y = move[0], move[1]
            time.sleep(.4) # to slow down the game
            
            if self.game.set_move(x, y, curr_player.val):
                if print_game:
                    print(f"{str(curr_player)} {[curr_player.letter]} makes a move to square {tuple(move)}")
                    self.game.print_board()
                    print()
                
                # Terminate if a player has won    
                if self.game.wins(curr_player.val):
                    winner = curr_player
                    break
                
                current_turn = 'X' if current_turn == 'O' else 'O'  # switches player
            else:
                raise RuntimeError("The selected move is invalid. There is a bug in the code!")
            
        # Game over message
        if winner != None:
            print(f'{winner} wins!')
        else:
            print("It's a draw!")
        exit()

############################################################################################################
import tkinter as tk
from tkinter import messagebox

class GameRender:
    def __init__(self, game, x_player, o_player, cell_size=60):
        self.game = game
        self.x_player = x_player
        self.o_player = o_player
        self.cell_size = cell_size
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe / Gomoku")
        self.canvas = tk.Canvas(self.root, width=self.game.SIZE * self.cell_size, height=self.game.SIZE * self.cell_size, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.current_player = self.x_player

        self.draw_board()

    def draw_board(self):
        for i in range(self.game.SIZE):
            for j in range(self.game.SIZE):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white", tags="square")
                mark = self.game.board_state[i][j]
                if mark == 1:
                    self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
                    self.canvas.create_line(x2, y1, x1, y2, fill="black", width=2)
                elif mark == -1:
                    self.canvas.create_oval(x1 + 2, y1 + 2, x2 - 2, y2 - 2, outline="black", fill="black")

    def cell_clicked(self, event):
        if not isinstance(self.current_player, Player):
            return  # Skip if current player is not human
        x, y = event.x // self.cell_size, event.y // self.cell_size
        move = self.current_player.get_move(self.game, x, y)
        if move and self.game.set_move(*move, self.current_player.val):
            self.draw_board()
            if self.game.game_over():
                winner = "Player O" if self.current_player.letter == 'X' else "Player X"
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.root.destroy()
            self.switch_player()
        else:
            messagebox.showerror("Error", "Invalid move!")

    def switch_player(self):
        self.current_player = self.o_player if self.current_player == self.x_player else self.x_player

    def run(self):
        self.root.mainloop()
                