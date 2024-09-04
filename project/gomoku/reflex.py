"""
TODO: Implement Approximate Q-Learning player for Gomoku.
* Extract features from the state-action pair and store in a numpy array.
* Define the size of the feature vector in the feature_size method.
"""

from ..player import Player

class GMK_Reflex(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        move = None
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return move
    
    def __str__(self):
        return "Reflex Player"
