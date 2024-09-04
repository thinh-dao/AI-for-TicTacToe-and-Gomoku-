"""
TODO: Implement improved version of MCTS player for Gomoku.
* You could try different tree policy, rollout policy, or other improvements.
"""

from ..player import Player
from ..game import Gomoku
import random

WIN = 1
LOSE = -1
DRAW = 0
NUM_SIMULATIONS = 5000

SEED = 2024
random.seed(SEED)

class GMK_BetterMTCS(Player):
    def __init__(self, letter, num_simulations=NUM_SIMULATIONS):
        super().__init__(letter)
        self.num_simulations = num_simulations
    
    def get_move(self, game: Gomoku):
        move = None
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return move
    
    def __str__(self) -> str:
        return "Better MTCS Player"
    