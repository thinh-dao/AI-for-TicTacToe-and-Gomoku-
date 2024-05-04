from typing import List, Optional
from abc import ABC, abstractmethod

class Game(ABC):
    
    @abstractmethod
    def empty_cells(self, state: Optional[List[List[int]]]) -> List[List[int]]:
        """
        Get a list of empty cells for the GIVEN state. If state is None, return the list of empty cells for the CURRENT state
        :param state: the state of the current board
        :return: a list of empty cells
        """
        pass
    
    @abstractmethod
    def print_board(self):
        """
        Visualization of current board state
        """
        pass
    
    @abstractmethod
    def init_board(self):
        """
        Print the board with empty cells
        """
        pass
    
    @abstractmethod
    def valid_move(self, x: int, y: int) -> bool:
        """
        Check if the cell (x,y) is a valid move.
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the move is valid
        """
        pass
    
    @abstractmethod
    def set_move(self, x: int, y: int, player_val: int) -> bool:
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player_val: Value of the current player
        """
        pass
    
    @abstractmethod
    def wins(self, player_val, state: Optional[List[List[int]]]) -> bool:
        """
        This function tests if a specific player wins in a GIVEN or CURRENT state (if state is None):
        :param state: the state of the current board
        :param player: a human or a computer
        :return: True if the player wins
        """
        pass
        
    @abstractmethod
    def game_over(self) -> bool:
        """
        This function test if the game is over for the current state
        :return: True if the game is over (either a player wins or the game is draw)
        """
        pass
    
class TicTacToe(Game):
    def __init__(self):
        self.board_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    def print_board(self):
        for row in self.board_state:
            print('-------------')
            for val in row:
                if val == 0:
                    print('|   ', end=''),
                elif val == 1:
                    print('| X ', end=''),
                elif val == -1:
                    print('| O ', end=''),
            print("|")
        print('-------------')

    @staticmethod
    def init_board():
        """
        Guideline for plain visualization mode"
        """
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        print("Guidelines:")
        for row in number_board:
            print('-------------')
            print('| ' + ' | '.join(row) + ' |')
        print('-------------\n')

    def empty_cells(self, state = None):
        cells = []
        if state == None:
            state = self.board_state # current state
            
        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])
        return cells
    
    def valid_move(self, x, y):
        if [x, y] in self.empty_cells(self.board_state):
            return True
        else:
            return False
    
    def set_move(self, x, y, player_val):
        if self.valid_move(x, y):
            self.board_state[x][y] = player_val
            return True
        else:
            return False

    def wins(self, player_val, state=None):
        """
        This function tests if a specific player wins in a GIVEN or CURRENT state. Possibilities:
        * Three rows    [X X X] or [O O O]
        * Three cols    [X X X] or [O O O]
        * Two diagonals [X X X] or [O O O]
        :param state: the state of the current board
        :param player: a human or a computer
        :return: True if the player wins
        """
        if state == None:
            state = self.board_state # current state
            
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player_val, player_val, player_val] in win_state:
            return True
        else:
            return False

    def game_over(self):
        return self.wins(-1, self.board_state) or self.wins(1, self.board_state) or len(self.empty_cells()) == 0
    