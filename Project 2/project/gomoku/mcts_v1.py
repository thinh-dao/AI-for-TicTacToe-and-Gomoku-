"""
TODO: Implement the standard MCTS player for Gomoku.
* tree policy: UCB1
* rollout policy: random
"""

import numpy as np
import math

from ..player import Player
from ..game import Gomoku

WIN = 1
LOSE = -1
DRAW = 0
NUM_SIMULATIONS = 5000

import random
SEED = 2024
random.seed(SEED)

class TreeNode():
    def __init__(self, game_state: Gomoku, player_letter: str, parent=None, parent_action=None):
        self.player = player_letter
        self.game_state = game_state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self.N = 0
        self.Q = 0
    
    def select(self) -> 'TreeNode':
        """
        Select the best child node based on UCB1 formula. Keep selecting until a leaf node is reached.
        """
        leaf_node = None
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return leaf_node
    
    def expand(self) -> 'TreeNode':
        """
        Expand the current node by adding all possible child nodes. Return one of the child nodes for simulation.
        """
        child_node = None
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return child_node
    
    def simulate(self) -> int:
        """
        Run simulation from the current node until the game is over. Return the result of the simulation.
        """
        result = 0
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return result
    
    def backpropagate(self, result: int):
        """
        Backpropagate the result of the simulation to the root node.
        """
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        pass
            
    def is_leaf_node(self) -> bool:
        return len(self.children) == 0
    
    def is_terminal_node(self) -> bool:
        return self.game_state.game_over()
    
    def best_child(self) -> 'TreeNode':
        return max(self.children, key=lambda c: c.ucb())
    
    def ucb(self, c=math.sqrt(2)) -> float:
        return self.Q / (1+self.N) + c * np.sqrt(np.log(self.parent.N) / (1+self.N))
    
class GMK_NaiveMCTS(Player):
    def __init__(self, letter, num_simulations=NUM_SIMULATIONS):
        super().__init__(letter)
        self.num_simulations = num_simulations
    
    def get_move(self, game: Gomoku):
        mtcs = TreeNode(game, self.letter)
        for num in range(self.num_simulations):
            leaf = mtcs.select()
            if not leaf.is_terminal_node():
                leaf.expand()
            result = leaf.simulate()
            leaf.backpropagate(-result)
            
        best_child = max(mtcs.children, key=lambda c: c.N)
        return best_child.parent_action
    
    def __str__(self) -> str:
        return "Naive MCTS Player"