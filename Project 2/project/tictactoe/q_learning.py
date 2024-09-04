import numpy as np
import random                                    
from ..player import Player
from ..game import TicTacToe
from ..player import RandomPlayer
from . import *
from tqdm import tqdm

NUM_EPISODES = 10000
LEARNING_RATE = 0.5
DISCOUNT_FACTOR = 0.9
EXPLORATION_RATE = 0.1

class TTT_QPlayer(Player):
    def __init__(self, letter, transfer_player=None):
        super().__init__(letter)
        self.opponent = transfer_player
        self.num_episodes = NUM_EPISODES
        self.learning_rate = LEARNING_RATE
        self.gamma = DISCOUNT_FACTOR
        self.epsilon = EXPLORATION_RATE
        self.Q = {}  
        self.action_history = []
    
    def train(self, game):
        # Main Q-learning algorithm
        opponent_letter = 'X' if self.letter == 'O' else 'O'
        if self.opponent is None:
            opponent = TTT_QPlayer(opponent_letter)
        else:
            opponent = self.opponent(opponent_letter)
            
        print(f"Training {self.letter} player for {self.num_episodes} episodes...")
        game_state = game.copy()
        
        for episode in tqdm(range(self.num_episodes)):               
            game_state.restart()
            opponent.action_history = []
            
            current_player = self if self.letter == 'X' else opponent 
            next_player = self if self.letter == 'O' else opponent
            
            while True:                
                if isinstance(current_player, TTT_QPlayer):
                    action = current_player.choose_action(game_state)
                    state = current_player.hash_board(game_state.board_state)
                    current_player.action_history.append((state, action)) 
                else:
                    action = current_player.get_move(game_state)
                
                next_game_state = game_state.copy()
                next_game_state.set_move(action[0], action[1], current_player.letter)
                
                if next_game_state.game_over():
                    reward = 1 if next_game_state.wins(current_player.letter) else -1 if next_game_state.wins(next_player.letter) else 0
                    if isinstance(current_player, TTT_QPlayer):
                        current_player.update_rewards(reward)
                    if isinstance(next_player, TTT_QPlayer):
                        next_player.update_rewards(-reward)
                    break
                else: 
                    current_player, next_player = next_player, current_player
                    game_state = next_game_state    
            
            self.letter = 'X' if self.letter == 'O' else 'O'
            opponent.letter = 'X' if opponent.letter == 'O' else 'O'    
            self.action_history = []    
    
    def update_rewards(self, reward):
        # Backpropagate rewards through the action history
        last_state, last_action = self.action_history[-1]
        self.update_q_table(last_state, last_action, last_state, reward)
        for t in range(len(self.action_history) -1, 0, -1):
            reward = self.gamma * reward
            next_state, _ = self.action_history[t]
            current_state, current_action = self.action_history[t - 1]
            self.update_q_table(current_state, current_action, next_state, reward)

    def choose_action(self, game):
        state = self.hash_board(game.board_state)
        game_state = np.array(game.board_state)
        # Exploration-exploitation trade-off
        if random.uniform(0, 1) < self.epsilon or state not in self.Q:
            action = random.choice(game.empty_cells())
        else:
            # Choose the action with the highest Q-value
            q_values = self.Q[state]
            empty_cells = np.argwhere(game_state == None)                           
            empty_q_values = [q_values[cell[0], cell[1]] for cell in empty_cells]      
            max_q_value = max(empty_q_values)                                          
            max_q_indices = [i for i in range(len(empty_cells)) if empty_q_values[i] == max_q_value]    
            max_q_index = random.choice(max_q_indices)                                 
            action = tuple(empty_cells[max_q_index])                                   
        return action
    
    def update_q_table(self, state, action, next_state, reward):
        next_q_values = self.Q.get(next_state, np.zeros((3, 3)))
        max_next_q_value = np.max(next_q_values)
        q_values = self.Q.get(state, np.zeros((3, 3)))        
        q_values[action[0], action[1]] += self.learning_rate * (reward + self.gamma * max_next_q_value - q_values[action[0], action[1]])
        self.Q[state] = q_values
    
    def hash_board(self, board):
        key = ''
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    key += '1'
                elif board[i][j] == 'O':
                    key += '2'
                else:
                    key += '0'
        return key

    def get_move(self, game: TicTacToe):
        self.epsilon = 0
        move = self.choose_action(game)
        return move
    
    def __str__(self):
        return "Q-Learning Player"