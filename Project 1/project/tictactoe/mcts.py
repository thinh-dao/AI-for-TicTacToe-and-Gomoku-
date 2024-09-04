"""
TODO: Implement the TreeNode for TTT_MCTSPlayer class.
* Note 1: You should read the game logic in project/game.py to familiarize yourself with the environment.
* Note 2: You don't have to strictly follow the template or even use it at all. Feel free to create your own implementation.
"""

import numpy as np
import math

from ..player import Player
from ..game import TicTacToe

WIN = 1
LOSE = -1
DRAW = 0
NUM_SIMULATIONS = 5000

class TreeNode():
    def __init__(self, game_state: TicTacToe, player_letter: str, parent=None, parent_action=None):
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
            
    def is_leaf_node(self) -> bool:
        return len(self.children) == 0
    
    def is_terminal_node(self) -> bool:
        return self.game_state.game_over()
    
    def best_child(self) -> 'TreeNode':
        return max(self.children, key=lambda c: c.ucb())
    
    def ucb(self, c=math.sqrt(2)) -> float:
        if self.N == 0:
            return float('inf')
        return self.Q / self.N + c * np.sqrt(np.log(self.parent.N) / self.N)
    
class TTT_MCTSPlayer(Player):
    def __init__(self, letter, num_simulations=NUM_SIMULATIONS):
        super().__init__(letter)
        self.num_simulations = num_simulations
    
    def get_move(self, game):
        mcts = TreeNode(game, self.letter)
        for _ in range(self.num_simulations):
            leaf = mcts.select()
            if not leaf.is_terminal_node():
                leaf.expand()
            # Default simulation starts from an expanded node of leaf. However, we can also start simulation from leaf itself to avoid complicating the code.
            result = leaf.simulate() 
            leaf.backpropagate(-result) # Negate the result because it's from the perspective of the opponent
            
        best_child = max(mcts.children, key=lambda c: c.N)
        return best_child.parent_action
    
    def __str__(self) -> str:
        return "MCTS Player"