from .game import TicTacToe, FiveInARow
from .gameplay import GamePlay
from .player import HumanPlayer, RandomPlayer, MinimaxPlayer, AlphaBetaPlayer

if __name__ == '__main__':
    x_player = MinimaxPlayer('X')
    o_player = HumanPlayer('O')
    tic_tac_toe = TicTacToe()
    
    gameplay = GamePlay(x_player=x_player, o_player=o_player, game=tic_tac_toe)
    gameplay.run()
    