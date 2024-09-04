from .game import TicTacToe
from .tictactoe import TTT_HumanPlayer, TTT_MinimaxPlayer, TTT_AlphaBetaPlayer, TTT_MCTSPlayer, TTT_QPlayer
from .player import RandomPlayer

def Game(game):
    if game == 'tictactoe':
        game = TicTacToe()
    else:
        raise ValueError("Invalid game. Please choose between 'tictactoe' and 'gomoku'")
    return game

def Player(player1, player2):
    if player1 == 'random':
        x_player = RandomPlayer('X')
    elif player1 == 'human':
        x_player = TTT_HumanPlayer('X')
    elif player1 == 'minimax':
        x_player = TTT_MinimaxPlayer('X')
    elif player1 == 'alphabeta':
        x_player = TTT_AlphaBetaPlayer('X')
    elif player1 == 'mcts':
        x_player = TTT_MCTSPlayer('X')
    elif player1 == 'qplayer':
        x_player = TTT_QPlayer('X')
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
    elif player2 == 'mcts':
        o_player = TTT_MCTSPlayer('O')
    elif player2 == 'qplayer':
        o_player = TTT_QPlayer('O')
    else:
        raise ValueError(f"Player 2 {player2} is not defined.")
            
    
    return x_player, o_player
