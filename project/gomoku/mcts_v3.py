"""
TODO: Implement AlphaGo version of MCTS for Gomoku.
* paper: https://www.davidsilver.uk/wp-content/uploads/2020/03/unformatted_final_mastering_go.pdf
* Some github repos for reference:
    *https://github.com/junxiaosong/AlphaZero_Gomoku
    *https://github.com/PolyKen/15_by_15_AlphaGomoku
"""

from ..player import Player
from ..game import Gomoku

WIN = 1
LOSE = -1
DRAW = 0
NUM_SIMULATIONS = 5000

import random
SEED = 2024
random.seed(SEED)
    
class GMK_AlphaGoMTCS(Player):
    def __init__(self, letter, num_simulations=NUM_SIMULATIONS):
        super().__init__(letter)
        self.num_simulations = num_simulations
    
    def get_move(self, game: Gomoku):
        move = None
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return move
    
    def __str__(self) -> str:
        return "AlphaGo MTCS Player"