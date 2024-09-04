"""
This module contains the game logic for Tic Tac Toe and Gomoku. 
* You may need to understand the code to implement your own players. 
! The code should not be modified.
"""
from typing import List, Optional
from abc import ABC, abstractmethod

class Game(ABC):
    
    @abstractmethod
    def empty_cells(self, state: Optional[List[List[int]]]) -> List[List[int]]:
        """
        Get a list of empty cells for the GIVEN state. If state is None, return the list of empty cells for the CURRENT state.
        :param state: the state of the current board
        :return: a list of empty cells
        """
        pass
    
    @abstractmethod
    def print_board(self):
        """
        Visualization of current board state.
        """
        pass
    
    @abstractmethod
    def init_board(self):
        """
        Draw the initial board and show the game info.
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
    def set_move(self, x: int, y: int, player_letter: str) -> bool:
        """
        Set the move on board, if the coordinates are valid.
        :param x: X coordinate
        :param y: Y coordinate
        :param player_letter: 'X' or 'O
        :return: True if the move is set successfully
        """
        pass

    @abstractmethod
    def wins(self, player_letter: str, state: Optional[List[List[int]]]) -> bool:
        """
        This function tests if a specific player wins in a GIVEN or CURRENT state (if state is None).
        :param state: the state of the current board
        :param player_letter: 'X' or 'O
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
    
    @abstractmethod
    def restart(self) -> None:
        """
        This function restarts the game
        """
        pass
    
    @abstractmethod
    def copy(self) -> 'Game':
        """
        This function returns a copy of the current game
        """
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        return "Game"
    
class TicTacToe(Game):
    def __init__(self):
        #* Initialize board, available moves, last move, and win_combo
        self.board_state = [[None, None, None], [None, None, None], [None, None, None]]
        self.win_combo = []
        self.curr_player = 'X'
    
    def print_board(self):
        height = len(self.board_state)
        width = len(self.board_state[0])
        
        for i in range(height):
            print('-------------')
            for j in range(width):
                if self.board_state[i][j] == None:
                    print('|   ', end='')
                elif self.board_state[i][j] == 'X':
                    print('| X ', end='')
                elif self.board_state[i][j] == 'O':
                    print('| O ', end='')
                else:
                    raise ValueError(f"Invalid value {self.board_state[i][j]} in the board")
            print("|")
        print('-------------')

    def init_board(self):
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        print("\nGame board:")
        for row in number_board:
            print('-------------')
            print('| ' + ' | '.join(row) + ' |')
        print('-------------\n')

    def empty_cells(self, state = None):
        cells = []
        if state == None:
            state = self.board_state
            
        for x in range(3):
            for y in range(3):
                if state[x][y] == None:
                    cells.append([x, y])
        return cells
    
    def valid_move(self, x, y):
        if self.board_state[x][y] == None:
            return True
        else:
            return False
    
    def set_move(self, x, y, player_letter):
        assert self.curr_player == player_letter, f"Invalid player {player_letter}. Current player is {self.curr_player}"
        if self.valid_move(x, y):
            self.board_state[x][y] = player_letter
            self.curr_player = 'X' if self.curr_player == 'O' else 'O'
            return True
        else:
            return False
    
    def reset_move(self, x, y):
        self.curr_player = self.board_state[x][y]
        self.board_state[x][y] = None

    def wins(self, player_letter, state=None):
        if state == None:
            state = self.board_state # current state
        
        # All possible winning states
        win_states = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)],
        ]
        
        for win_state in win_states:
            moves = set([state[x][y] for x, y in win_state])
            if len(moves) == 1 and player_letter in moves:
                self.win_combo = win_state
                return True
        return False

    def game_over(self):
        return self.wins('X') or self.wins('O') or len(self.empty_cells()) == 0
    
    def restart(self):
        self.board_state = [[None, None, None], [None, None, None], [None, None, None]]
        self.last_move = (-1, -1)
        self.win_combo = []
        self.curr_player = 'X'
        
    def copy(self):
        new_game = TicTacToe()
        new_game.board_state = [row[:] for row in self.board_state]
        new_game.win_combo = self.win_combo.copy()
        new_game.curr_player = self.curr_player
        return new_game
    
    def __str__(self) -> str:
        return "Tic Tac Toe"
        