"""
TODO: Implement Minimax with Alpha-Beta Pruning player for Gomoku.
* You need to implement heuristic evaluation function for non-terminal states.
* Optional: You can implement the function promising_next_moves to explore reduce the branching factor.
"""
from ..player import Player
from ..game import Gomoku
from typing import List, Tuple, Union
import math
import random
SEED = 2024
random.seed(SEED)

DEPTH = 2 # Define the depth of the search tree.

class GMK_AlphaBetaPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.depth = DEPTH 
    
    def get_move(self, game: Gomoku):
        if game.last_move == (-1, -1):
            mid_size = game.size // 2
            moves = [(mid_size, mid_size), (mid_size - 1, mid_size - 1), (mid_size + 1, mid_size + 1), (mid_size - 1, mid_size + 1), (mid_size + 1, mid_size - 1)]
            move = random.choice(moves)
            while not game.valid_move(move[0], move[1]):
                move = random.choice(moves)
            return move 
        else:
            # Alpha-Beta Pruning: Initialize alpha to negative infinity and beta to positive infinity
            alpha = -math.inf
            beta = math.inf
            choice = self.minimax(game, self.depth, self.letter, alpha, beta)
            move = [choice[0], choice[1]]
        return move

    def minimax(self, game, depth, player_letter, alpha, beta) -> Union[List[int], Tuple[int]]:
        """
        AI function that chooses the best move with alpha-beta pruning.
        :param game: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9)
        :param player_letter: value representing the player
        :param alpha: best value that the maximizer can guarantee
        :param beta: best value that the minimizer can guarantee
        :return: a list or a tuple with [best row, best col, best score]
        """
        move = [-1, -1]
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return move
    
    def evaluate(self, game, state=None) -> float:
        """
        Define a heuristic evaluation function for the given state when leaf node is reached.
        :return: a float value representing the score of the state
        """
        score = 0
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return score
    
    def promising_next_moves(self, game, player_letter) -> List[Tuple[int]]:
        """
        Find the promosing next moves to explore, so that the search space can be reduced.
        :return: a list of tuples with the best moves
        """
        moves = []
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return moves
    
    def __str__(self):
        return "AlphaBeta Player"
