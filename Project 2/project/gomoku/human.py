from ..player import Player

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