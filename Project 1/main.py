from project.gameplay import GamePlay
from project import Game, Player


import argparse

if __name__ == '__main__':
    
    # Initialize Argument Parser for command line arguments
    parser = argparse.ArgumentParser(description='Play Tic Tac Toe')
    parser.add_argument('--game', '-g', type=str, default='tictactoe', help='Choose the game to play')
    parser.add_argument('--player1', '-p1', type=str, default='human', choices=['minimax', 'alphabeta', 'mcts', 'qlearning', 'human', 'random'], help='Choose player 1')
    parser.add_argument('--player2', '-p2', type=str, default='random', choices=['minimax', 'alphabeta', 'mcts', 'qlearning', 'human', 'random'], help='Choose player 2')
    parser.add_argument('--mode', '-m', type=str, default='plain', choices=['silent', 'plain', 'ui'], help='Choose visualization mode')
    parser.add_argument('--num_games', '-n', type=int, default=1, help='Number of games to run')
    parser.add_argument('--timeout', '-t', type=int, default=10, help='Timeout for each move')
    parser.add_argument('--no_timeout', '-nt', action='store_true', help='No timeout for each move')
    args = parser.parse_args()
    
    if args.mode == 'silent' and (args.player1 == 'human' or args.player2 == 'human'):
        raise ValueError("Silent mode is not available for Human Player! Please choose between 'plain' and 'ui' modes.")
    
    if args.no_timeout:
        timeout = None
    else:
        timeout = args.timeout
        
    game, (x_player, o_player) = Game(game=args.game), Player(player1=args.player1, player2=args.player2)
    
    # Train Q-Learning Player
    if args.player1 == 'qplayer':
        x_player.train(game)
    if args.player2 == 'qplayer':
        o_player.train(game)
        
    gameplay = GamePlay(x_player=x_player, o_player=o_player, game=game, mode=args.mode, num_games=args.num_games, timeout=timeout)
    gameplay.run()

