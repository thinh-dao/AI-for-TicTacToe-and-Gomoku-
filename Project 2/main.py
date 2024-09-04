from project.gameplay import GamePlay
from project import Game, Player


import argparse

if __name__ == '__main__':
    
    # Initialize Argument Parser for command line arguments
    parser = argparse.ArgumentParser(description='Play Tic Tac Toe or Gomoku')
    parser.add_argument('--game', '-g', type=str, default='gomoku', choices=['tictactoe', 'gomoku'], help='Choose the game to play (tictactoe or gomoku)')
    parser.add_argument('--player1', '-p1', type=str, default='random', help='Choose player 1')
    parser.add_argument('--player2', '-p2', type=str, default='human', help='Choose player 2')
    parser.add_argument('--mode', '-m', type=str, default='plain', choices=['silent', 'plain', 'ui'], help='Choose visualization mode')
    parser.add_argument('--num_games', '-n', type=int, default=1, help='Number of games to run')
    parser.add_argument('--timeout', '-t', type=int, default=10, help='Timeout for each move')
    parser.add_argument('--no_timeout', '-nt', action='store_true', help='No timeout for each move')
    parser.add_argument('--size', '-s', type=int, default=15, help='Size of the board (only for Gomoku)')
    parser.add_argument('--load', '-l', type=str, default=None, help='Load weight file for Tabular/Approximate Q-Learning Player')
    parser.add_argument('--no_train', action='store_true', help='No training for Q-Learning Player')
    args = parser.parse_args()
    
    assert args.size >= 5, "Board size must be at least 5x5"
    if args.mode == 'silent' and (args.player1 == 'human' or args.player2 == 'human'):
        raise ValueError("Silent mode is not available for Human Player! Please choose between 'plain' and 'ui' modes.")
    
    if args.no_timeout:
        timeout = None
    else:
        timeout = args.timeout
    
    # Define game and players
    game = Game(args)

    x_player = Player(args, player=args.player1, letter='X')
    o_player = Player(args, player=args.player2, letter='O')
    
    if 'Q-Learning' in str(x_player):
        if args.load is not None:
            valid_size = f'{args.size}x{args.size}'
            print(valid_size)
            if not args.load.startswith(valid_size):
                invalid_size = args.load.split('_')[0]
                raise ValueError(f'The weight file is used for {invalid_size} board, but the board for evaluation is {valid_size}. Please use the weight file for {valid_size} board.')
            x_player.load_weight(args.load)
        if args.no_train == False:
            x_player.train(game)

    if 'Q-Learning' in str(o_player):
        if args.load is not None:
            valid_size = f'{args.size}x{args.size}'
            if not args.load.startswith(valid_size):
                invalid_size = args.load.split('_')[0]
                raise ValueError(f'The weight file is used for {invalid_size} board, but the board for evaluation is {valid_size}. Please use the weight file for {valid_size} board.')
            o_player.load_weight(args.load)
        if args.no_train == False:
            o_player.train(game)
        
    gameplay = GamePlay(x_player=x_player, o_player=o_player, game=game, mode=args.mode, num_games=args.num_games, timeout=timeout)
    gameplay.run()
