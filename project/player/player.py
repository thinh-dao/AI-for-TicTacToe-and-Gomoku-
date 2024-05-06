"""
This module contains Generic Player class and Random Player class.
"""
from ..game import Game
import random
from typing import Union, List, Tuple
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, letter: str):
        """
        Initialize the player with a letter (X or O).
        :param letter: X or O
        """
        assert (letter.upper() == 'X' or letter.upper() == 'O'), "Letter can only be X or O!"
        self.letter = letter.upper()

    @abstractmethod
    def get_move(self, game: Game) -> Union[List[int], Tuple[int, int]]:
        """
        Given current state of the game, return the next move in the form of (x, y) coordinates.
        :param game: Current game state
        :return: (x,y) or [x,y] as the selected move
        """
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """
        Name of the player.
        """
        return "Generic Player"
        
    
class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = random.choice(list(game.avail_moves))
        return move
    
    def __str__(self) -> str:
        return "Random Player"