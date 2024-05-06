from .game import TicTacToe, Gomoku
from .player import *

def Game(game):
    if game == 'tictactoe':
        game = TicTacToe()
    elif game == 'gomoku':
        game = Gomoku()
    else:
        raise ValueError("Invalid game. Please choose between 'tictactoe' and 'gomoku'")
    return game

def Player(game, player1, player2):
    if game == 'tictactoe':
        if game == 'random':
            x_player = RandomPlayer('X')
        elif player1 == 'human':
            x_player = TTT_HumanPlayer('X')
        elif player1 == 'minimax':
            x_player = TTT_MinimaxPlayer('X')
        elif player1 == 'alphabeta':
            x_player = TTT_AlphaBetaPlayer('X')
        else:
            raise ValueError(f"Player 1 {player1} is not defined.")
        
        if player2 == 'random':
            o_player = RandomPlayer('O')
        elif player2 == 'human':
            o_player = TTT_HumanPlayer('O')
        elif player2 == 'minimax':
            o_player = TTT_MinimaxPlayer('O')
        elif player2 == 'alphabeta':
            o_player = TTT_AlphaBetaPlayer('O')
        else:
            raise ValueError(f"Player 2 {player2} is not defined.")
    elif game == 'gomoku':
        if player1 == 'random':
            x_player = RandomPlayer('X')
        elif player1 == 'human':
            x_player = GMK_HumanPlayer('X')
        elif player1 == 'minimax':
            x_player = GMK_MinimaxPlayer('X')
        elif player1 == 'alphabeta':
            x_player = GMK_AlphaBetaPlayer('X')
        else:
            raise ValueError(f"Player 1 {player1} is not defined.")
        
        if player2 == 'random':
            o_player = RandomPlayer('O')
        elif player2 == 'human':
            o_player = GMK_HumanPlayer('O')
        elif player2 == 'minimax':
            o_player = GMK_MinimaxPlayer('O')
        elif player2 == 'alphabeta':
            o_player = GMK_AlphaBetaPlayer('O')
        else:
            raise ValueError(f"Player 2 {player2} is not defined.")
    return x_player, o_player
