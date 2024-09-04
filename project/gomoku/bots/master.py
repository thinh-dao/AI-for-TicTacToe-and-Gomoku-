"""
* Threat Space Search (TSS) Player for Gomoku
* Implementation based on: https://github.com/xavierwwj/Gomoku-AI--Python-
* Paper: https://cdn.aaai.org/Symposia/Fall/1993/FS-93-02/FS93-02-001.pdf

This AI will decide a move based on the following order of steps:
(0) -> If AI can win this turn, AI does so
(1) -> Check for opponent's threats and prevent them (the straight_four
threat cannot be prevented so we will not check for this threat type)
(2) -> Form a winning threat-sequence independent of opponent's movement
        (we will ignore the proof-number search for now and allow opponent
        to place seeds on all cost squares)
(3) -> Prevent opponent from forming a threat (prevention is better than
        cure). There may be multiple squares to prevent multiple threats
        so we count all and see which square has the most occurances. This
        can be done by treating own colour as opponent. If placing on a
        square results in a threat being formed, then that square is a
        prevention square.
(4) -> Lastly, we will place our seed where our seeds are most in-line.
        Calculation: total seeds in-line excluding where seed is placed.
        If turn 1 => place beside opponent's. Also if multiple squares
        have equal total, randomly select a square.
"""

from typing import List, Tuple
import numpy as np
import random
import copy
from ...player import Player

EMPTY = 0
X = 1
O = 2

def convert_board(board):
    board_np = np.array(board)
    board_np[board_np == 'X'] = X
    board_np[board_np == 'O'] = O
    board_np[board_np == None] = EMPTY
    return board_np.astype(int)

class GMK_Master(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.board = None
        self.AI = AI()
        self.found_sol = False
        self.sol_seq = [] 

        self.p1_c = O if self.letter == 'X' else X
        self.AI_c = X if self.letter == 'X' else O
    
    def get_move(self, game) -> List[int] | Tuple[int, int]:
        self.board = convert_board(copy.deepcopy(game.board_state))

        if np.sum(self.board) == 0:  # the board is empty and AI first
            return game.size // 2, game.size // 2
        elif np.sum(self.board) == 1:  # the board is not empty and AI second
            row, column = np.where(self.board == self.p1_c)[0][0], np.where(self.board == self.p1_c)[1][0]
            # If row index > column index i.e. bottom left triangle,
            # then place on top of opponent seed. Vice versa
            mid_size = len(self.board) // 2 - 1
            if row >= mid_size and column >= mid_size:
                return random.choice([[row-1, column-1], [row-1, column], [row, column-1]])
            elif row >= mid_size and column < mid_size:
                return random.choice([[row-1, column], [row-1, column+1], [row, column+1]])
            elif row < mid_size and column >= mid_size:
                return random.choice([[row+1, column], [row+1, column-1], [row, column-1]]) 
            else:
                return random.choice([[row+1, column+1], [row+1, column], [row, column+1]])

        AI_pos = None

        if self.found_sol:
            # if len(self.sol_seq) > 0:
            #     AI_pos = self.sol_seq.pop(0)
            # else:
            self.found_sol = False  # reset  
            x = self.AI.find_threats(5, self.p1_c, game.size, self.board)
            y = self.AI.find_threats(6, self.p1_c, game.size, self.board)
            z = self.AI.find_threats(7, self.p1_c, game.size, self.board)

            merged_threat = dict()
            if x:
                merged_threat.update(x)
            if y:
                merged_threat.update(y)
            if z:
                merged_threat.update(z)

            if merged_threat:
                AI_pos = min(merged_threat, key=merged_threat.get)
        else:
            x = self.AI.find_threats(5, self.p1_c, game.size, self.board)
            y = self.AI.find_threats(6, self.p1_c, game.size, self.board)
            z = self.AI.find_threats(7, self.p1_c, game.size, self.board)

            merged_threat = dict()
            if x:
                merged_threat.update(x)
            if y:
                merged_threat.update(y)
            if z:
                merged_threat.update(z)

            if merged_threat:
                AI_pos = min(merged_threat, key=merged_threat.get)
            else:
                root_node = self.AI.node(None)
                sol = self.AI.threat_space_search(self.board, root_node, self.p1_c, self.AI_c, game.size)
                if sol:
                    self.found_sol = True
                    self.sol_seq = sol[1:]
                    AI_pos = self.sol_seq.pop(0)
                else:
                    AI_pos = self.AI.maximise_own(game, self.letter)
        
        if AI_pos == None or self.board[AI_pos[0], AI_pos[1]] != EMPTY:
            AI_pos = self.AI.maximise_own(game, self.letter)
        return AI_pos
    
    def restart(self):
        self.board = None
        self.AI = AI()
        self.found_sol = False
        self.sol_seq = [] 

        self.p1_c = O if self.letter == 'X' else X
        self.AI_c = X if self.letter == 'X' else O

    def __str__(self):
        return "Master Player"
    
class AI:

    def __init__(self):
        self.get_opp = {
            X: O,
            O: X,
        }

    # Defining of all threat variations
    def four(self, array, colour):
        # accepts an array of length 5
        # 11110 or 01111 or 10111 or 11011 or 11101
        x = list(array)
        if x.count(colour) == 4 and x.count(EMPTY) == 1:
            return [True, x.index(EMPTY)]
        return [False]

    def broken_three(self, array, colour):
        # accepts an array of length 6
        # 010110 or 011010 (flip!)
        if array[0] == EMPTY and array[1] == colour and \
                array[5] == EMPTY and array[4] == colour:
            if array[2] == EMPTY and array[3] == colour:
                return [True, 2]
            elif array[2] == colour and array[3] == EMPTY:
                return [True, 3]
        return [False]

    def three(self, array, colour):
        # accepts an array of length 7
        opp = self.get_opp[colour]
        # 0011100 or 2011100 or 0011102
        if array[2] == colour and array[3] == colour and array[4] == colour and array[5] == EMPTY and array[1] == EMPTY:
            if array[0] == EMPTY and array[6] == EMPTY:
                return [True, 1, 5]
            elif array[0] == opp and array[6] == EMPTY:
                return [True, 1, 5, 6]
            elif array[0] == EMPTY and array[6] == opp:
                return [True, 1, 5, 0]
        return [False]

    def straight_four(self, array, colour):
        # accepts an array of length 6
        # 011110
        if array[0] == EMPTY and array[5] == EMPTY and array[1] == colour and \
                array[2] == colour and array[3] == colour and array[4] == colour:
            return True
        return False

    def five(self, array, colour):
        # accepts an array of length 5
        # 11111
        x = list(array)
        if x.count(colour) == 5:
            return True
        return False

    ###################
    ## Section (0+1) ##
    ###################

    def threat_algo(self, array, colour, length):
        ## colour = player's colour by default
        opp = self.get_opp[colour]
        if length == 5:
            x = self.four(array, opp)
            if x[0]:  # if opp has a four
                x.append(1)
                return x
            x = self.four(array, colour)
            if x[0]:  # if AI has a four
                x.append(2)
                return x
        elif length == 6:
            x = self.broken_three(array, opp)
            if x[0]:  # if opp has a broken-three
                x.append(3)
                return x
            x = self.broken_three(array, colour)
            if x[0]:  # if AI has a broken-three
                x.append(5)
                return x
        elif length == 7:
            x = self.three(array, opp)
            if x[0]:  # if opp has a three
                y = random.choice([x[1], x[2]])
                # y = x[1]
                return [True, y, 4]
            x = self.three(array, colour)
            if x[0]:  # if AI has a three
                y = random.choice([x[1], x[2]])
                # y = x[1]
                return [True, y, 6]
        return [False]

    def find_threats(self, length, colour, size, board):
        threat_list = {}
        ## Read horizontally
        for row in range(size):
            for col in range(size-(length-1)):
                array = board[row,col:col+length]
                i = self.threat_algo(array,colour, length)
                if i[0] == True:
                    threat_list.update({(row,col+i[1]): i[2]})              
                
        ## Read vertically
        for col in range(size):
            for row in range(size-(length-1)):
                array = board[row:row+length,col]
                i = self.threat_algo(array,colour, length)
                if i[0]  ==  True:
                    threat_list.update({(row+i[1],col): i[2]})              
                
        ## Read diagonally
        for row in range(size-(length-1)):
            for col in range(size-(length-1)):
                array = []
                for i in range(length):
                    array.append(board[i+row,i+col])
                i = self.threat_algo(array,colour, length)
                if i[0]  == True:
                    threat_list.update({(row+i[1],col+i[1]): i[2]})               

                array = []
                for i in range(length):
                    array.append(board[i+row,col+length-1-i])
                i = self.threat_algo(array,colour, length)
                if i[0] == True:
                    threat_list.update({(row+i[1],col+length-1-i[1]): i[2]})              
        if len(threat_list.keys()) == 0:
            return False
        else:
            return threat_list

    #################
    ## Section (2) ##
    #################

    class node:
        def __init__(self, val):
            self.val = val
            self.children = []
            self.parent = False
            self.sol = None

        def set_child(self, child_node):
            self.children.append(child_node)

        def set_parent(self, parent_node):
            self.parent = parent_node

        def set_sol(self, node):
            self.sol = node

    def threat_space_search(self, board, root_node, p1_c, AI_c, size):
        found_sol = False
        sol_seq = []

        def store_seq(leaf_node):
            nonlocal sol_seq
            sol_seq.insert(0, leaf_node.val)
            if leaf_node.parent:
                store_seq(leaf_node.parent)

        def make_threats(old_board, root_node, parent_node, depth):
            ### Calling this func takes in a root node and initial board,
            ### loops through each square, place stone on square and check
            ### for any threats made. If a single threat is found, then
            ### update modified_board with the cost squares. Add that board
            ### to new_boards list. As long as winning sol is not found and
            ### there are some new boards, recursively call make_threats()
            ### until a sol is found or no more possible threats can be
            ### sequenced up.
            nonlocal found_sol
            nonlocal sol_seq
            vicinity = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1],
                        [-2, 0], [0, -2], [0, 2], [2, 0], [2, 2], [-2, -2], [2, -2], [-2, 2],
                        [1, -2], [-1, -2], [1, 2], [-1, 2], [2, -1], [-2, -1], [2, 1], [-2, 1]]
            
            if depth < 3:
                new_boards = []
                for i in range(size):
                    for j in range(size):
                        if old_board[i][j] == EMPTY:
                            search = False
                            for each in vicinity:
                                adjacent_cell = [i + each[0], j + each[1]]
                                if 0 <= adjacent_cell[0] < size and 0 <= adjacent_cell[1] < size and old_board[adjacent_cell[0]][adjacent_cell[1]] == AI_c:
                                    search = True
                                    break

                            if not search:
                                continue

                            modified_board = np.copy(old_board)
                            modified_board[i][j] = AI_c
                            a = loop_board(size, 5, AI_c, modified_board, 0)
                            b = loop_board(size, 6, AI_c, modified_board, 0)
                            c = loop_board(size, 7, AI_c, modified_board, 0)
                            merged_threat_list = a + b + c
                            if len(merged_threat_list) == 1:
                                x = self.node([i, j])
                                x.set_parent(parent_node)
                                parent_node.set_child(x)
                                for each in merged_threat_list[0]:
                                    modified_board[each[0]][each[1]] = p1_c
                                new_boards.append([modified_board, x])
                            elif len(merged_threat_list) == 2:
                                # a secondary confirmation as a double
                                # threat may have been found but in fact
                                # the cost square of one interferes with the
                                # solution of the other

                                confirmed = False
                                confirmed2 = False
                                for t in merged_threat_list[0]:
                                    sol_board = np.copy(modified_board)
                                    sol_board[t[0], t[1]] = p1_c
                                for p in merged_threat_list[1]:
                                    if not confirmed:
                                        if sol_board[p[0], p[1]] == EMPTY:
                                            sol_board1 = np.copy(sol_board)
                                            sol_board1[p[0], p[1]] = AI_c
                                            if loop_board(size, 5, AI_c, sol_board1, 1) or loop_board(size, 6, AI_c, sol_board1, 1):
                                                confirmed = True
                                if confirmed:
                                    for t in merged_threat_list[1]:  # assuming double-threat only
                                        sol_board = np.copy(modified_board)
                                        sol_board[t[0], t[1]] = p1_c
                                    for p in merged_threat_list[0]:
                                        if not confirmed2:
                                            if sol_board[p[0], p[1]] == EMPTY:
                                                sol_board1 = np.copy(sol_board)
                                                sol_board1[p[0], p[1]] = AI_c
                                                if loop_board(size, 5, AI_c, sol_board1, 1) or loop_board(size, 6, AI_c, sol_board1, 1):
                                                    confirmed2 = True

                                if confirmed and confirmed2:
                                    x = self.node([i, j])
                                    x.set_parent(parent_node)
                                    parent_node.set_child(x)
                                    root_node.set_sol(merged_threat_list)
                                    sol_seq = []
                                    store_seq(x)
                                    found_sol = True
                                    ##for each in merged_threat_list:
                                    ##    y = self.node(each)
                                    ##    y.set_parent(x)
                                    ##    x.set_child(y)

                if len(new_boards) != 0 and found_sol == False:
                    for each in new_boards:
                        make_threats(each[0], root_node, each[1], depth + 1)

        def loop_board(size, length, colour, board, spec) -> list | bool:
            ### Iterates through the board, returns a list of
            ### lists of cost_squares, each sub-list corresponding
            ### to a threat in the modified board.
            ### Note that it can be more efficient by just checking
            ### the vicinity of the position AI_c was placed at
            threat_list = []
            for row in range(size):
                for col in range(size-(length-1)):
                    array = board[row,col:col+length]
                    if spec == 0:
                        i = win_algo(array,colour, length)
                        if i[0] == True:
                            cost_squares = []
                            for each in i[1]:
                                cost_squares.append([row,col+each])
                            threat_list.append(copy.deepcopy(cost_squares))
                    else:
                        x = sol_algo(array, colour, length)
                        if x:
                            return x
                    
            for col in range(size):
                for row in range(size-(length-1)):
                    array = board[row:row+length,col]
                    if spec == 0:
                        i = win_algo(array,colour, length)
                        if i[0]  ==  True:
                            cost_squares = []
                            for each in i[1]:
                                cost_squares.append([row+each,col])
                            threat_list.append(copy.deepcopy(cost_squares))
                    else:
                        x = sol_algo(array, colour, length)
                        if x:
                            return x
                    
            for row in range(size-(length-1)):
                for col in range(size-(length-1)):
                    array = []
                    for i in range(length):
                        array.append(board[i+row,i+col])
                    if spec == 0:
                        i = win_algo(array,colour, length)
                        if i[0]  == True:
                            cost_squares = []
                            for each in i[1]:
                                cost_squares.append([row+each,col+each])
                            threat_list.append(copy.deepcopy(cost_squares))          
                    else:
                        x = sol_algo(array, colour, length)
                        if x:
                            return x
                        
                    array = []
                    for i in range(length):
                        array.append(board[i+row,col+length-1-i])
                    if spec == 0:
                        i = win_algo(array,colour, length)
                        if i[0] == True:
                            cost_squares = []
                            for each in i[1]:
                                cost_squares.append([row+each,col+length-1-each])
                            threat_list.append(copy.deepcopy(cost_squares))
                    else:
                        x = sol_algo(array, colour, length)
                        if x:
                            return x
            if spec == 0:
                return threat_list
            else:
                return False

        def win_algo(array, colour, length):
            ### Check if a threat formation is found, returns True and
            ### the cost squares if found
            if length == 5:
                x = self.four(array, colour)
                if x[0]:
                    return [True, [x[1]]]
            elif length == 6:
                x = self.broken_three(array, colour)
                if x[0]:
                    return [True, [x[1]]]
            elif length == 7:
                x = self.three(array, colour)
                if x[0]:
                    return [True, x[1:]]
            return [False]

        def sol_algo(array, colour, length):
            if length == 5:
                return self.five(array, colour)
            elif length == 6:
                return self.straight_four(array, colour)
            else:
                return False

        make_threats(board, root_node, root_node, 0)
        if found_sol:
            return sol_seq
        else:
            return False

    #################
    ## Section (4) ##
    #################
    
    def maximise_own(self, game, AI_c):
        board = convert_board(copy.deepcopy(game.board_state))
        score = {}
        for row, col in np.ndindex(board.shape):
            if board[row, col] == EMPTY:
                score.update(self.check_surroundings(board, AI_c, row, col))

        v = list(score.values())
        k = list(score.keys())
        m = max(v)
        indices = [i for i, j in enumerate(v) if j == m]
        best_score = []

        for each in indices:
            if k[each][0] >= 0 and k[each][1] >= 0:
                best_score.append(k[each])

        return random.choice(best_score)

    def check_surroundings(self, board, colour, row, col):
        ## Basically, given a possible position you can place your seed,
        ## calculate the score i.e. no. of consecutive seeds in all directions

        sub_score = 0  # how many consecutive seeds (directionless)
        score = 0
        empty_counter = 0

        def check_neighbour(original_row, original_col, row, col, direction, side, prev_is_empty):
            def num_to_dir(argument):
                def TLBR():
                    return [[row - 1, col - 1], [row + 1, col + 1]]

                def TRBL():
                    return [[row - 1, col + 1], [row + 1, col - 1]]

                def HORZ():
                    return [[row, col - 1], [row, col + 1]]

                def VERT():
                    return [[row - 1, col], [row + 1, col]]

                switcher = {
                    1: TLBR,
                    2: TRBL,
                    3: HORZ,
                    4: VERT,
                }
                func = switcher.get(argument)
                return func()

            try:
                nonlocal sub_score
                nonlocal score
                nonlocal empty_counter
                if colour == X:
                    opp = O
                else:
                    opp = X

                # SIDE 0 (vs SIDE 1)
                if side == 0:
                    new_row = num_to_dir(direction)[0][0]
                    new_col = num_to_dir(direction)[0][1]
                elif side == 1:
                    new_row = num_to_dir(direction)[1][0]
                    new_col = num_to_dir(direction)[1][1]

                if new_row < 0:
                    new_row = 13
                elif new_col < 0:
                    new_col = 13
                ## if original_row == 3 and original_col == 4:
                ##     print("R: ",new_row, "C: ", new_col)
                if board[new_row, new_col] == colour:
                    if empty_counter == 1:
                        sub_score += 0.9
                    else:
                        sub_score += 1
                    check_neighbour(original_row, original_col, new_row, new_col, direction, side, False)
                elif board[new_row, new_col] == EMPTY and empty_counter < 1:
                    ## We would only want to check up to 1 empty square beyond
                    empty_counter += 1
                    check_neighbour(original_row, original_col, new_row, new_col, direction, side, True)
                elif board[new_row, new_col] == EMPTY and empty_counter == 1:
                    ## Flip side
                    if side == 0:
                        empty_counter = 0
                        check_neighbour(original_row, original_col, original_row, original_col, direction, 1, False)
                    else:
                        score += sub_score
                        sub_score = 0
                        empty_counter = 0
                elif board[new_row, new_col] == opp:
                    if prev_is_empty:
                        ## Flip side
                        if side == 0:
                            empty_counter = 0
                            check_neighbour(original_row, original_col, original_row, original_col, direction, 1, False)
                        else:
                            score += sub_score
                            sub_score = 0
                            empty_counter = 0
                    else:
                        sub_score = 0
                        empty_counter = 0
            except IndexError:
                if side == 0:
                    # Flip side
                    empty_counter = 0
                    check_interference(original_row, original_col, original_row, original_col, direction, 1)
                else:
                    score += sub_score
                    sub_score = 0
                    empty_counter = 0

        def check_interference(original_row, original_col, row, col, direction, side):
            def num_to_dir(argument):
                def TLBR():
                    return [[row - 1, col - 1], [row + 1, col + 1]]

                def TRBL():
                    return [[row - 1, col + 1], [row + 1, col - 1]]

                def HORZ():
                    return [[row, col - 1], [row, col + 1]]

                def VERT():
                    return [[row - 1, col], [row + 1, col]]

                switcher = {
                    1: TLBR,
                    2: TRBL,
                    3: HORZ,
                    4: VERT,
                }
                func = switcher.get(argument)
                return func()

            try:
                nonlocal score
                nonlocal sub_score
                nonlocal empty_counter

                if colour == X:
                    opp = O
                else:
                    opp = X
                    # SIDE 0 (vs SIDE 1)
                if side == 0:
                    new_row = num_to_dir(direction)[0][0]
                    new_col = num_to_dir(direction)[0][1]
                elif side == 1:
                    new_row = num_to_dir(direction)[1][0]
                    new_col = num_to_dir(direction)[1][1]
                if new_row < 0:
                    new_row = 15
                elif new_col < 0:
                    new_col = 15

                ## if original_row == 3 and original_col == 0:
                ##     print("R: ",new_row, "C: ",new_col) 
                if board[new_row, new_col] == opp:
                    if empty_counter == 1:
                        sub_score += 0.9
                    else:
                        sub_score += 1
                    check_interference(original_row, original_col, new_row, new_col, direction, side)
                elif board[new_row, new_col] == EMPTY and empty_counter < 1:
                    empty_counter += 1
                    check_interference(original_row, original_col, new_row, new_col, direction, side)
                elif board[new_row, new_col] == colour:
                    ## If you hit into your own seed, it means you're
                    ## already blocking opponent, if any. So ignore
                    sub_score = 0
                    empty_counter = 0
                else:
                    if side == 0:
                        # Flip side
                        empty_counter = 0
                        check_interference(original_row, original_col, original_row, original_col, direction, 1)
                    else:
                        score += sub_score
                        sub_score = 0
                        empty_counter = 0
            except IndexError:
                if side == 0:
                    # Flip side
                    empty_counter = 0
                    check_interference(original_row, original_col, original_row, original_col, direction, 1)
                else:
                    score += sub_score
                    sub_score = 0
                    empty_counter = 0

        ## Check for all directions individually
        for i in range(4):
            check_neighbour(row, col, row, col, i + 1, 0, False)

            ## If my pieces are less than opponent
            ## => I gain advantage by interfering,
            ## more so than I lose out from being interfered.
            ## Hence we need to consider this special case and add it to score

            check_interference(row, col, row, col, i + 1, 0)

        return {(row, col): score}
    