import time
from player import Player
from game import Game

class GamePlay():
    def __init__(self, x_player: Player, o_player: Player, game: Game):
        """
        Three modes for visualization of the game:
        1. "silent": game play is not shown (Not available for Human Player)
        2. "plain": game play is shown in terminal
        3. "ui": game play is shown in UI        
        """
        self.board_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_winner = None
        self.x_player = x_player
        self.o_player = o_player
        
        # Check player initialization
        assert (self.x_player.letter == 'X'), "Wrong letter initialization for X Player!"
        assert (self.o_player.letter == 'O'), "Wrong letter initialization for O Player"
        
        self.game = game
    
    def run(self, print_game=True):
        if print_game:
            self.game.init_board()

        current_turn = 'X'
        winner = None
        
        while len(self.game.empty_cells()) > 0:
            if current_turn == 'X':
                curr_player = self.x_player
            else:
                curr_player = self.o_player
                
            move = curr_player.get_move(self.game)
            x, y = move[0], move[1]
            time.sleep(.4) # to slow down the game
            
            if self.game.set_move(x, y, curr_player.val):
                if print_game:
                    print(f"{str(curr_player)} {[curr_player.letter]} makes a move to square {move}")
                    self.game.print_board()
                    print()
                
                # Terminate if a player has won    
                if self.game.wins(curr_player.val):
                    winner = curr_player
                    break
                
                current_turn = 'X' if current_turn == 'O' else 'O'  # switches player
            else:
                raise RuntimeError("The selected move is invalid. There is a bug in the code!")
            
        # Game over message
        if winner != None:
            print(f'{winner} wins!')
        else:
            print("It's a draw!")
        exit()
        