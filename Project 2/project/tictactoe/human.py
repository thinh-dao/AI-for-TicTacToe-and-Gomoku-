"""
This module contains the Player classes for Tic Tac Toe game.
TODO: Implement the MinimaxPlayer class.
* Note: You should read the game logic in project/game.py to familiarize yourself with the environment.
"""
import numpy as np
from collections import defaultdict
from ..player import Player
from ..game import TicTacToe

class TTT_HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Dictionary of valid moves
        move = -1
        moves = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 9: (2, 2),
        }
        # Get input move from human
        while move < 1 or move > 9:
            try:
                move = int(input(f"Human move [{self.letter}] (1..9): "))
                x, y = moves[move]
                can_move = game.valid_move(x, y)

                if not can_move:
                    print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')
        return moves[move]
    
    def __str__(self) -> str:
        return "Human Player"

