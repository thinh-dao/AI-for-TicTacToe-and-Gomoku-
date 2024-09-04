"""
TODO: Implement the TTT_MinimaxPlayer class.
* Note 1: You should read the game logic in project/game.py to familiarize yourself with the environment.
* Note 2: You don't have to strictly follow the template or even use it at all. Feel free to create your own implementation.
"""

from typing import List, Tuple, Union
import random
import math
from ..player import Player
from ..game import TicTacToe

class TTT_MinimaxPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game: TicTacToe) -> Union[List[int], Tuple[int, int]]:
        depth = len(game.empty_cells())
        
        if depth == 9:
            move = random.choice(list(game.empty_cells())) # Random move if it's the first move
        else:
            move = self.minimax(game, depth, self.letter)
        
        return move

    def minimax(self, game: TicTacToe, depth: int, player_letter: str) -> Union[List[int], Tuple[int, int]]:
        """
        Minimax algorithm that chooses the best move
        :param game: current game state
        :param depth: node index in the tree (0 <= depth <= 9), but never 9 in this case
        :param player_letter: value representing the player
        :return: (row, col) of the selected move
        """
        best = None
        ######### YOUR CODE HERE #########
        

        
        ######### YOUR CODE HERE #########
        return best
    
    def evaluate(self, game: TicTacToe) -> int:
        """
        Function to evaluate the score of game state.
        :param game: the game state to evaluate
        :return: the score of the board from the perspective of current player
        """
        score = 0
        ######### YOUR CODE HERE #########
        

        
        ######### YOUR CODE HERE #########
        return score
    
    def __str__(self) -> str:
        return "Minimax Player"