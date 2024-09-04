from .game import *
from .tictactoe import *
from .gomoku import *
from .player import *

def Game(args):
    if args.game == 'tictactoe':
        game = TicTacToe()
    elif args.game == 'gomoku':
        game = Gomoku(args.size)
    else:
        raise ValueError("Invalid game. Please choose between 'tictactoe' and 'gomoku'")
    return game

def Player(args, player, letter):
    if args.game == 'tictactoe':
        if player == 'random':
            agent = RandomPlayer(letter)
        elif player == 'human':
            agent = TTT_HumanPlayer(letter)
        elif player == 'minimax':
            agent = TTT_MinimaxPlayer(letter)
        elif player == 'alphabeta':
            agent = TTT_AlphaBetaPlayer(letter)
        elif player == 'mcts':
            agent = TTT_MTCSPlayer(letter)
        elif player == 'qplayer':
            agent = TTT_QPlayer(letter)
        else:
            raise ValueError(f"{player} is not defined for {args.game.capitalize()}.")
            
    elif args.game == 'gomoku':
        if player == 'random':
            agent = RandomPlayer(letter)
        elif player == 'human':
            agent = GMK_HumanPlayer(letter)
        elif player == 'alphabeta':
            agent = GMK_AlphaBetaPlayer(letter)
        elif player == 'mcts_v1':
            agent = GMK_NaiveMTCS(letter)
        elif player == 'mcts_v2':
            agent = GMK_BetterMTCS(letter)
        elif player == 'mcts_v3':
            agent = GMK_AlphaGoMTCS(letter)
        elif player == 'qplayer_v1':
            agent = GMK_TabularQPlayer(letter, size=args.size)
        elif player == 'qplayer_v2':
            agent = GMK_ApproximateQPlayer(letter, size=args.size)
        elif player == 'beginner':
            agent = GMK_Beginner(letter)
        elif player == 'intermediate':
            agent = GMK_Intermediate(letter)
        elif player == 'advanced':
            agent = GMK_Advanced(letter)
        elif player == 'master':
            agent = GMK_Master(letter)
        else:
            raise ValueError(f"{player.capitalize()} player is not defined for {args.game.capitalize()}.")
        
    return agent
