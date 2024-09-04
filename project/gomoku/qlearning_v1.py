"""
TODO: Implement Tabular Q-Learning player for Gomoku.
* After training, Q-table is saved in q_table/{size}x{size}_{num_episodes}.pkl file.
* To load the q-table, use the --load flag with the filename.
* To run your q-learning player without training, use the --no_train flag.
"""

import numpy as np
import random
import pickle
import os
from typing import List, Tuple, Union
from tqdm import tqdm
from ..player import Player

NUM_EPISODES = 10000
LEARNING_RATE = 0.01
DISCOUNT_FACTOR = 0.9
EXPLORATION_RATE = 0.1

class GMK_TabularQPlayer(Player):
    def __init__(self, letter, size=15, transfer_player=None):
        super().__init__(letter)
        self.opponent = transfer_player
        self.num_episodes = NUM_EPISODES
        self.learning_rate = LEARNING_RATE
        self.gamma = DISCOUNT_FACTOR
        self.epsilon = EXPLORATION_RATE
        self.Q = {}  
        self.action_history = []
        self.board_size = size

    def train(self, game, save_filename=None):
        # Main Q-learning algorithm
        opponent_letter = 'X' if self.letter == 'O' else 'O'
        if self.opponent is None:
            opponent = GMK_TabularQPlayer(opponent_letter)
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
                if isinstance(current_player, GMK_TabularQPlayer):
                    action = current_player.choose_action(game_state)
                    state = current_player.hash_board(game_state.board_state)
                    current_player.action_history.append((state, action)) 
                else:
                    action = current_player.get_move(game_state)
                
                next_game_state = game_state.copy()
                next_game_state.set_move(action[0], action[1], current_player.letter)
                
                if next_game_state.game_over():
                    reward = 1 if next_game_state.wins(current_player.letter) else -1 if next_game_state.wins(next_player.letter) else 0
                    if isinstance(current_player, GMK_TabularQPlayer):
                        current_player.update_rewards(reward)
                    if isinstance(next_player, GMK_TabularQPlayer):
                        next_player.update_rewards(-reward)
                    break
                else: 
                    current_player, next_player = next_player, current_player
                    game_state = next_game_state    
            
            self.letter = 'X' if self.letter == 'O' else 'O'
            opponent.letter = 'X' if opponent.letter == 'O' else 'O'    
            self.action_history = []    

        print("Training complete. Saving Q-table...")
        if save_filename is None:
            save_filename = f'{self.board_size}x{self.board_size}_{NUM_EPISODES}.pkl'
        self.save_weight(save_filename)
    
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
        next_q_values = self.Q.get(next_state, np.zeros((self.board_size, self.board_size)))
        max_next_q_value = np.max(next_q_values)
        q_values = self.Q.get(state, np.zeros((self.board_size, self.board_size)))       
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
    
    def save_weight(self, filename):
        """
        Save the Q-table.
        """
        path = 'project/gomoku/q_table'
        os.makedirs(path, exist_ok=True)
        with open(f'{path}/{filename}', 'wb') as f:
            pickle.dump(self.Q, f)

    def load_weight(self, filename):
        """
        Load the Q-table.
        """
        path = 'project/gomoku/q_table'
        if not os.path.exists(f'{path}/{filename}'):
            raise FileNotFoundError(f"Q-table file '{filename}' not found.")
        with open(f'{path}/{filename}', 'rb') as f:
            self.Q = pickle.load(f)

    def get_move(self, game):
        self.epsilon = 0  # No exploration
        return self.choose_action(game)

    def __str__(self):
        return "Tabular Q-Learning Player"
