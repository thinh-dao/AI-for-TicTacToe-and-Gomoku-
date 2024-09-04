"""
TODO: Implement the standard MCTS player for Gomoku.
* tree policy: UCB1
* rollout policy: random
"""

import numpy as np
import math
import random

from ..player import Player
from ..game import Gomoku

WIN = 1
LOSE = -1
DRAW = 0
NUM_SIMULATIONS = 2000

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
        current_node = self
        while not current_node.is_leaf_node():
            current_node = current_node.best_child()
        return current_node
    
    def expand(self) -> 'TreeNode':
        possible_moves = self.game_state.empty_cells()
        for move in possible_moves:
            child_game_state = self.game_state.copy()
            child_game_state.set_move(move[0], move[1], self.player)
            child_player = 'X' if self.player == 'O' else 'O'
            child_node = TreeNode(child_game_state, child_player, parent=self, parent_action=move)
            self.children.append(child_node)
    
    def simulate(self) -> int:
        player_letter = self.player
        opponent_letter = 'X' if player_letter == 'O' else 'O'
        
        curr_letter = player_letter
        simulate_game = self.game_state.copy()
        
        while True:             
            if simulate_game.wins(player_letter):
                return WIN
            elif simulate_game.wins(opponent_letter):
                return LOSE
            elif len(simulate_game.empty_cells()) == 0:
                return DRAW
            else:  
                move = random.choice(simulate_game.empty_cells())
                simulate_game.set_move(move[0], move[1], curr_letter)
                curr_letter = 'X' if curr_letter == 'O' else 'O'
    
    def backpropagate(self, result):
        if self.parent:
            self.parent.backpropagate(-result)
        self.N += 1
        self.Q += result
            
    def is_leaf_node(self) -> bool:
        return len(self.children) == 0
    
    def is_terminal_node(self) -> bool:
        return self.game_state.game_over()
    
    def best_child(self) -> 'TreeNode':
        return max(self.children, key=lambda c: c.ucb())
    
    def ucb(self, c=math.sqrt(2)) -> float:
        return self.Q / (1+self.N) + c * np.sqrt(np.log(self.parent.N) / (1+self.N))
    
class GMK_NaiveMTCS(Player):
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
        return "Naive MTCS Player"