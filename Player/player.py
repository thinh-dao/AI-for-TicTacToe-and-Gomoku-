import random
from ..game import Game
from typing import List
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, letter: str):
        assert (letter.upper() == 'X' or letter.upper() == 'O'), "Letter can only be X or O!"
        self.letter = letter.upper()
        if self.letter == 'X': 
            self.val = 1
        else:
            self.val = -1

    @abstractmethod
    def get_move(self, game: Game) -> List[int]:
        pass
    
class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = random.choice(game.empty_cells())
        return move
    
    def __str__(self) -> str:
        return "Random Player"