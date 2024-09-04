"""
TODO: Implement the MinimaxPlayer class.
* Note: You should read the game logic in project/game.py to familiarize yourself with the environment.
"""

import random
import math
from ..player import Player
from ..game import TicTacToe

class TTT_MinimaxPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game: TicTacToe):
        depth = len(game.empty_cells())
        
        if depth == 9:
            move = random.choice(list(game.empty_cells()))
        else:
            choice = self.minimax(game, depth, self.letter)
            move = [choice[0], choice[1]]
        
        return move

    def minimax(self, game, depth, player_letter):
        """
        Minimax algorithm that chooses the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9), but never 9 in this case
        :param player_letter: value representing the player
        :return: a list with [best row, best col, best score]
        """
        if player_letter == self.letter:
            best = [-1, -1, -math.inf] # Max Player
        else:
            best = [-1, -1, +math.inf] # Min Player

        if depth == 0 or game.game_over():
            score = self.evaluate(game)
            return [-1, -1, score]

        for cell in game.empty_cells():
            x, y = cell[0], cell[1]
            game.set_move(x, y, player_letter)
            other_letter = 'X' if player_letter == 'O' else 'O'
            score = self.minimax(game, depth - 1, other_letter)
            game.reset_move(x, y)
            score[0], score[1] = x, y

            if player_letter == self.letter:
                if score[2] > best[2]:
                    best = score  # Max value
            else:
                if score[2] < best[2]:
                    best = score  # Min value
        return best
    
    def evaluate(self, game, state=None):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: (+1 * EMPTY_STATES) if the computer wins; (-1 * EMPTY_STATES) if the human wins; 0 if draw
        """
        other_letter = 'X' if self.letter == 'O' else 'O'
        if game.wins(self.letter, state):
            score = +1 * (len(game.empty_cells()) + 1)
        elif game.wins(other_letter, state):
            score = -1 * (len(game.empty_cells()) + 1)
        else:
            score = 0
        return score
    
    def __str__(self) -> str:
        return "Minimax Player"