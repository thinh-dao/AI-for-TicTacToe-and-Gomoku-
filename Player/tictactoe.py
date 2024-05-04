import random
import math
from typing import List
from .player import Player

class MinimaxPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        depth = len(game.empty_cells())
        print(f'Computer turn [{self.letter}]')
        
        if depth == 9:
            move = random.choice(game.empty_cells())
        else:
            choice = self.minimax(game, depth, self.val)
            move = [choice[0], choice[1]]
        return move

    def minimax(self, game, depth, player_val):
        """
        Minimax algorithm that chooses the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9), but never 9 in this case
        :param player_val: value representing the player
        :return: a list with [best row, best col, best score]
        """
        if player_val == self.val:
            best = [-1, -1, -math.inf] # Max Player
        else:
            best = [-1, -1, +math.inf] # Min Player

        if depth == 0 or game.game_over():
            score = self.evaluate(game)
            return [-1, -1, score]

        for cell in game.empty_cells():
            x, y = cell[0], cell[1]
            game.board_state[x][y] = player_val
            score = self.minimax(game, depth - 1, -player_val)
            game.board_state[x][y] = 0
            score[0], score[1] = x, y

            if player_val == self.val:
                if score[2] > best[2]:
                    best = score  # Max value
            else:
                if score[2] < best[2]:
                    best = score  # Min value
        return best
    
    def evaluate(self, game, state=None):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: (+1 * EMPTY_STATES) if the computer wins; (-1 * EMPTY_STATES) if the human wins; 0 if draw
        """
        if game.wins(self.val, state):
            score = +1 * (len(game.empty_cells()) + 1)
        elif game.wins(-self.val, state):
            score = -1 * (len(game.empty_cells()) + 1)
        else:
            score = 0
        return score
    
    def __str__(self) -> str:
        return "Minimax Player"
    
class AlphaBetaPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        depth = len(game.empty_cells())
        if depth == 0 or game.game_over():
            return
        
        print(f'Computer turn [{self.letter}]')
        
        if len(game.empty_cells()) == 9:
            move = random.choice(game.empty_cells())
        else:
            # Alpha-Beta Pruning: Initialize alpha to negative infinity and beta to positive infinity
            alpha = -math.inf
            beta = math.inf
            choice = self.minimax(game, depth, self.val, alpha, beta)
            move = [choice[0], choice[1]]
        return move

    def minimax(self, game, depth, player_val, alpha, beta) -> List[int]:
        """
        AI function that chooses the best move with alpha-beta pruning.
        :param game: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9)
        :param player_val: value representing the player
        :param alpha: best value that the maximizer can guarantee
        :param beta: best value that the minimizer can guarantee
        :return: a list with [best row, best col, best score]
        """
        if player_val == self.val:
            best = [-1, -1, -math.inf]  # Max Player
        else:
            best = [-1, -1, +math.inf]  # Min Player

        if depth == 0 or game.game_over():
            score = self.evaluate(game)
            return [-1, -1, score]

        for cell in game.empty_cells():
            x, y = cell[0], cell[1]
            game.board_state[x][y] = player_val
            score = self.minimax(game, depth - 1, -player_val, alpha, beta)
            game.board_state[x][y] = 0
            score[0], score[1] = x, y

            if player_val == self.val:  # Max player
                if score[2] > best[2]:
                    best = score
                alpha = max(alpha, best[2])
                if beta <= alpha:
                    break
            else:  # Min player
                if score[2] < best[2]:
                    best = score
                beta = min(beta, best[2])
                if beta <= alpha:
                    break
        return best
    
    def evaluate(self, game, state=None):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: (+1 * EMPTY_STATES) if the computer wins; (-1 * EMPTY_STATES) if the human wins; 0 if draw
        """
        if game.wins(self.val, state):
            score = +1 * (len(game.empty_cells()) + 1)
        elif game.wins(-self.val, state):
            score = -1 * (len(game.empty_cells()) + 1)
        else:
            score = 0
        return score
    
    def __str__(self) -> str:
        return "Alpha-Beta Player"
    