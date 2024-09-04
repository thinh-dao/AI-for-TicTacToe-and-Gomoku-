"""
* Naive agent that only focuses on attacking moves
"""

EMPTY = None
import random
SEED = 2024
random.seed(SEED)
import numpy as np
import copy

from ...player import Player

class GMK_Beginner(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if game.last_move == (-1, -1):
            mid_size = game.size // 2
            moves = [(mid_size, mid_size), (mid_size - 1, mid_size - 1), (mid_size + 1, mid_size + 1), (mid_size - 1, mid_size + 1), (mid_size + 1, mid_size - 1)]
            move = random.choice(moves)
            while not game.valid_move(move[0], move[1]):
                move = random.choice(moves)
            return move 
        else:
            return self.reflex_agent(game)
        
    def reflex_agent(self, game):
        valid_moves = game.empty_cells()
        scoring = dict()
        # Check for winning moves
        for move in valid_moves:
            if self.is_winning_move(game, move[0], move[1], self.letter):
                return move
        for move in valid_moves:
            if self.is_straight_four(game, move[0], move[1], self.letter):
                return move
        for move in valid_moves:
            scoring[tuple(move)] = self.heuristic(game.board_state, self.letter, move[0], move[1])
        
        best_score = max(scoring.values())
        best_moves = [move for move in scoring.keys() if scoring[move] == best_score]
        best_move = random.choice(best_moves)
        return best_move
    
    def straight_four(self, player, array):
        if array[0] == EMPTY and array[5] == EMPTY and array[1] == player and \
                array[2] == player and array[3] == player and array[4] == player:
            return True
        return False
    
    def is_winning_move(self, game, x, y, player):
        modified_game = game.copy()
        modified_game.set_move(x, y, player)
        return modified_game.wins(player)
    
    def is_straight_four(self, game, x, y, player):
        board = np.array(copy.deepcopy(game.board_state))
        board[x][y] = player
        size = len(board)
        length = 6
        for row in range(size):
            for col in range(size-(length-1)):
                array = board[row,col:col+length]
                is_threat = self.straight_four(player, array)
                if is_threat: 
                    return True            
                    
        ## Read vertically
        for col in range(size):
            for row in range(size-(length-1)):
                array = board[row:row+length,col]
                is_threat = self.straight_four(player, array)
                if is_threat: 
                    return True

        ## Read diagonally
        for row in range(size-(length-1)):
            for col in range(size-(length-1)):
                array = []
                for i in range(length):
                    array.append(board[i+row,i+col])
                is_threat = self.straight_four(player, array)
                if is_threat: 
                    return True             

                array = []
                for i in range(length):
                    array.append(board[i+row,col+length-1-i])
                is_threat = self.straight_four(player, array)
                if is_threat: 
                    return True
        return False
    
    def heuristic(self, board, player, row, col):
        modified_board = copy.deepcopy(board)
        modified_board[row][col] = player
        board_size = len(board)

        max_count = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

        for dr, dc in directions:
            count = 1
            for i in range(1, 5):
                r, c = row + i * dr, col + i * dc
                if 0 <= r < board_size and 0 <= c < board_size and modified_board[r][c] == player:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                r, c = row - i * dr, col - i * dc
                if 0 <= r < board_size and 0 <= c < board_size and modified_board[r][c] == player:
                    count += 1
                else:
                    break
            max_count += count
        return max_count
    
    def __str__(self):
        return "Beginner Player"
