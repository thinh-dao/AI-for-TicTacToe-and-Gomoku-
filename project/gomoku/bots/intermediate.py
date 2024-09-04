"""
* Priority of moves:
1. Winning move
2. Blocking opponent's winning move
3. Straight four
4. Blocking opponent's straight four
5. Constructing moves with the most threats
"""
EMPTY = None
import random
import numpy as np
import copy

from ...player import Player

class GMK_Intermediate(Player):
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
        opponent = 'X' if self.letter == 'O' else 'O'
        valid_moves = game.empty_cells()
        
        scoring = dict()
        # Check for winning moves
        for move in valid_moves:
            if self.is_winning_move(game, move[0], move[1], self.letter):
                return move
        for move in valid_moves:    
            if self.is_winning_move(game, move[0], move[1], opponent):
                return move
        for move in valid_moves:
            if self.is_straight_four(game, move[0], move[1], self.letter):
                return move
        for move in valid_moves:
            if self.is_straight_four(game, move[0], move[1], opponent):
                return move
        for move in valid_moves:
            modified_board = np.array(copy.deepcopy(game.board_state))
            modified_board[move[0], move[1]] = self.letter

            move = tuple(move)
            scoring[move] = 0
            scoring[move] += self.find_threats(5, self.letter, modified_board)
            scoring[move] += self.find_threats(6, self.letter, modified_board)
            scoring[move] += self.find_threats(7, self.letter, modified_board)
            
        max_num_threats = max(scoring.values())
        possible_moves = [move for move in scoring.keys() if scoring[move] == max_num_threats]
        best_move = max(possible_moves, key=lambda move: self.heuristic(game.board_state, self.letter, move[0], move[1]) + self.heuristic(game.board_state, opponent, move[0], move[1]))
        return best_move
    
    def find_threats(self, length, player, board):
        threat_cnt = 0
        size = len(board)
        for row in range(size):
            for col in range(size-(length-1)):
                array = board[row,col:col+length]
                is_threat = self.get_threat(player, array)
                if is_threat: 
                    threat_cnt += 1              
                    
        ## Read vertically
        for col in range(size):
            for row in range(size-(length-1)):
                array = board[row:row+length,col]
                is_threat = self.get_threat(player, array)
                if is_threat: 
                    threat_cnt += 1

        ## Read diagonally
        for row in range(size-(length-1)):
            for col in range(size-(length-1)):
                array = []
                for i in range(length):
                    array.append(board[i+row,i+col])
                is_threat = self.get_threat(player, array)
                if is_threat: 
                    threat_cnt += 1              

                array = []
                for i in range(length):
                    array.append(board[i+row,col+length-1-i])
                is_threat = self.get_threat(player, array)
                if is_threat: 
                    threat_cnt += 1 
        return threat_cnt
    
    def get_threat(self, player, array):
        # blocked four: OXXXX_
        if len(array) == 5:
            x = list(array)
            if x.count(player) == 4 and x.count(EMPTY) == 1:
                return True
            return False
        
        # broken three: _X_XX_ or _XX_X_
        elif len(array) == 6:
            if array[0] == EMPTY and array[1] == player and array[5] == EMPTY and array[4] == player:
                if (array[2] == EMPTY and array[3] == player):
                    return True
                elif (array[2] == player and array[3] == EMPTY):
                    return True
            return False
        
        # Open three: _XXX_
        elif len(array) == 7:
            opp = 'X' if player == 'O' else 'O'
            if array[1] == EMPTY and array[2] == player and array[3] == player and array[4] == player and array[5] == EMPTY:
                if array[0] == EMPTY and array[6] == EMPTY:
                    return True
                elif array[0] == opp and array[6] == EMPTY:
                    return True
                elif array[0] == EMPTY and array[6] == opp:
                    return True
            return False
    
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
        return "Intermediate Player"
