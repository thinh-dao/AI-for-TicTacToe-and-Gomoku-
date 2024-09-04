"""
TODO: Implement Approximate Q-Learning player for Gomoku.
* Extract features from the state-action pair and store in a dictionary with the format {feature_name: feature_value}.
* Similarly, the weight will be the dictionary in the format {feature_name: weight_value}.
* Define the size of the feature vector in the feature_size method.
"""
from typing import List, Tuple, Union, DefaultDict
from tqdm import tqdm
from ..player import Player
from collections import defaultdict

import numpy as np
import os
import pickle

NUM_EPISODES = 100000
LEARNING_RATE = 0.01
DISCOUNT_FACTOR = 0.9
EXPLORATION_RATE = 0.1

class GMK_ApproximateQPlayer(Player):
    def __init__(self, letter, size=15, transfer_player=None):
        super().__init__(letter)
        self.opponent = transfer_player
        self.num_episodes = NUM_EPISODES
        self.learning_rate = LEARNING_RATE
        self.gamma = DISCOUNT_FACTOR
        self.epsilon = EXPLORATION_RATE
        self.weights = defaultdict(lambda: 0) # Initialize weights to 0
        self.action_history = []
        self.board_size = size
        self.feature_extractor = SimpleExtractor()

    def train(self, game):
        # Main Q-learning algorithm
        opponent_letter = 'X' if self.letter == 'O' else 'O'
        if self.opponent is None:
            opponent = GMK_ApproximateQPlayer(opponent_letter)
        else:
            opponent = self.opponent(opponent_letter)
            
        print(f"Training {self.letter} player for {self.num_episodes} episodes...")
        game_state = game.copy()
        
        for _ in tqdm(range(self.num_episodes)):               
            game_state.restart()
            self.action_history = []
            opponent.action_history = []
            
            current_player = self if self.letter == 'X' else opponent 
            next_player = self if self.letter == 'O' else opponent
            
            while True:                
                if isinstance(current_player, GMK_ApproximateQPlayer):
                    action = current_player.choose_action(game_state)
                    state = current_player.hash_board(game_state.board_state)
                    current_player.action_history.append((state, action)) 
                else:
                    action = current_player.get_move(game_state)
                
                next_game_state = game_state.copy()
                next_game_state.set_move(action[0], action[1], current_player.letter)
                
                if next_game_state.game_over():
                    reward = 1 if next_game_state.wins(current_player.letter) else -1 if next_game_state.wins(next_player.letter) else 0
                    if isinstance(current_player, GMK_ApproximateQPlayer):
                        current_player.update_rewards(reward)
                    if isinstance(next_player, GMK_ApproximateQPlayer):
                        next_player.update_rewards(-reward)
                    break
                else: 
                    current_player, next_player = next_player, current_player
                    game_state = next_game_state    
            
            self.letter = 'X' if self.letter == 'O' else 'O'
            opponent.letter = 'X' if opponent.letter == 'O' else 'O'  
        
        print("Training complete. Saving training weights...")
        if save_filename is None:
            save_filename = f'{self.board_size}x{self.board_size}_{NUM_EPISODES}.pkl'
        self.save_weight(save_filename)
    
    def update_rewards(self, reward: float):
        """
        Given the reward at the end of the game, update the weights for each state-action pair in the game with the TD update rule:
            for weight w_i of feature f_i for (s, a):
                w_i = w_i + alpha * (reward + gamma * Q(s', a') - Q(s, a)) * f_i(s, a)
        * We need to update the Q-values for each state-action pair in the action history because the reward is only received at the end.
        """
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        pass

    def choose_action(self, game) -> Union[List[int], Tuple[int, int]]:
        """
        Choose action with ε-greedy strategy.
        If random number < ε, choose random action.
        Else choose action with the highest Q-value.
        :return: action
        """
        action = None
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        return action

    def update_q_values(self, state, action, next_state, reward):
        """
        Given (s, a, s', r), update the weights for the state-action pair (s, a) using the TD update rule:
            w = w + alpha * (reward + gamma * max(Q(s', a')) - Q(s, a)) * feature(s, a)
        :return: None
        """
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        pass

    def feature_vector(self, state, action) -> np.ndarray:
        """
        Extract the feature vector for a given state-action pair.
        :return: feature vector
        """
        return self.feature_extractor(state, action, self.letter)

    def feature_size(self) -> int:
        """
        Define the size of the feature vector.
        :return: size of the feature vector
        """
        ######### YOUR CODE HERE #########
        
        ######### YOUR CODE HERE #########
        pass

    def q_value(self, state, action) -> float:
        """
        Compute the Q-value for a given state-action pair as the dot product of the feature vector and the weight vector.
        :return: Q-value
        """
        q_value = 0
        features = self.feature_vector(state, action)
        for feature_name in features.keys():
            q_value += self.weights[feature_name] * features[feature_name]
        return q_value

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
        Save the weights of the feature vector.
        """
        path = 'project/gomoku/q_weights'
        os.makedirs(path, exist_ok=True)
        with open(f'{path}/{filename}', 'wb') as f:
            pickle.dump(self.weights, f)

    def load_weight(self, filename):
        """
        Load the Q-table.
        """
        path = 'project/gomoku/q_weights'
        if not os.path.exists(f'{path}/{filename}'):
            raise FileNotFoundError(f"Weight file '{filename}' not found.")
        with open(f'{path}/{filename}', 'rb') as f:
            self.weights = pickle.load(f)

    def get_move(self, game):
        self.epsilon = 0  # No exploration
        return self.choose_action(game)

    def __str__(self):
        return "Approximate Q-Learning Player"

########################### Feature Extractor ###########################
from abc import ABC, abstractmethod
import copy

class FeatureExtractor(ABC):
    @abstractmethod
    def getFeatures(self, state: List[List[str]], move: Union[List[int], Tuple[int]], player: str) -> DefaultDict[str, float]:
        """
        :param state: current board state
        :param move: move taken by the player
        :param player: current player
        :return: a dictionary {feature_name: feature_value}
        """
        pass

class IdentityExtractor(FeatureExtractor):
    def getFeatures(self, state, move, player):
        feats = defaultdict(lambda: 0.0)
        feats[(state, move)] = 1.0
        return feats

class SimpleExtractor(FeatureExtractor):
    def getFeatures(self, state, move, player):
        """
        features: #-of-unblocked-three-player, #-of-unblocked-three-opponent
        """
        opponent = 'X' if player == 'O' else 'O'
        state_modified = copy.deepcopy(state)

        x, y = move
        state_modified[x][y] = player

        feats = defaultdict(lambda: 0.0)
        feats['#-of-unblocked-three-player'] = self.check_open_three(player, state)
        feats['#-of-unblocked-three-opponent'] = self.check_open_three(player, opponent)
        feats['bias'] = 1.0
        
        return feats
    
    def check_open_three(self, player, board):
        length = 5
        def check_open_three(player, array):
            return array.count(player) == 3 and array.count(None) < 2
        
        threat_cnt = 0
        size = len(board)
        for row in range(size):
            for col in range(size-(length-1)):
                array = board[row,col:col+length]
                is_threat = check_open_three(player, array)
                if is_threat: 
                    threat_cnt += 1              
                    
        ## Read vertically
        for col in range(size):
            for row in range(size-(length-1)):
                array = board[row:row+length,col]
                is_threat = check_open_three(player, array)
                if is_threat: 
                    threat_cnt += 1

        ## Read diagonally
        for row in range(size-(length-1)):
            for col in range(size-(length-1)):
                array = []
                for i in range(length):
                    array.append(board[i+row,i+col])
                is_threat = check_open_three(player, array)
                if is_threat: 
                    threat_cnt += 1              

                array = []
                for i in range(length):
                    array.append(board[i+row,col+length-1-i])
                is_threat = check_open_three(player, array)
                if is_threat: 
                    threat_cnt += 1 

        return threat_cnt
    