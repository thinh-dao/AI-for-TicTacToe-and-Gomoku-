"""
This module contains the Player classes for Gomoku game.
TODO: Implement Gomoku players. You can implement more than one player for each type.
* Note: You should read the game logic in project/game.py to familiarize yourself with the environment.
"""

from .player import Player

class GMK_HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Get input move from human
        move = None
        while move == None:
            try:
                move = list(map(int, input(f"Human move [{self.letter}]: ").split(",")))
                x, y = move[0], move[1]
                can_move = game.valid_move(x, y)

                if not can_move:
                    print('Bad move')
                    move = None
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')
        return move
    
    def __str__(self) -> str:
        return "Human Player"
    
class GMK_BadPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass
    
    def __str__(self) -> str:
        return "Naive Player"
    
class GMK_NormalPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass
    
    def __str__(self) -> str:
        return "Naive Player"
    
class GMK_MinimaxPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass
    
    def __str__(self):
        return "Minimax Player"
    
class GMK_AlphaBetaPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass
    
    def __str__(self):
        return "AlphaBeta Player"
    
    