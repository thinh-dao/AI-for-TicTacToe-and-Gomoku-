from project.gameplay import GamePlay
from project import Game, Player

import argparse

if __name__ == '__main__':
    
    # Initialize Argument Parser for command line arguments
    parser = argparse.ArgumentParser(description='Play Tic Tac Toe or Gomoku')
    parser.add_argument('--game', '-g', type=str, default='tictactoe', choices=['tictactoe', 'gomoku'], help='Choose the game to play (tictactoe or gomoku)')
    parser.add_argument('--player1', '-p1', type=str, default='random', help='Choose player 1')
    parser.add_argument('--player2', '-p2', type=str, default='human', help='Choose player 2')
    parser.add_argument('--mode', '-m', type=str, default='plain', choices=['silent', 'plain', 'ui'], help='Choose visualization mode')
    parser.add_argument('--num_games', '-n', type=int, default=1, help='Number of games to run')
    parser.add_argument('--timeout', '-t', type=int, default=5, help='Timeout for each move')
    args = parser.parse_args()
    
    if args.mode == 'silent' and (args.player1 == 'human' or args.player2 == 'human'):
        raise ValueError("Silent mode is not available for Human Player! Please choose between 'plain' and 'ui' modes.")
    
    game, (x_player, o_player)  = Game(game=args.game), Player(game=args.game, player1=args.player1, player2=args.player2)
    gameplay = GamePlay(x_player=x_player, o_player=o_player, game=game, mode=args.mode)
    gameplay.run()

