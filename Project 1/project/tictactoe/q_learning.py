"""
TODO: Implement the TTT_QPlayer class.
* Note 1: You should read the game logic in project/game.py to familiarize yourself with the environment.
* Note 2: You don't have to strictly follow the template or even use it at all. Feel free to create your own implementation.
"""               
from typing import List, Tuple, Union             
from ..player import Player
from ..game import TicTacToe
from . import *
from tqdm import tqdm

NUM_EPISODES = 100000
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
        """
        Train the Q-Learning player against an transfer player to update the Q tables.
        """
        opponent_letter = 'X' if self.letter == 'O' else 'O'
        if self.opponent is None:
            opponent = TTT_QPlayer(opponent_letter)
        else:
            opponent = self.opponent(opponent_letter)
            
        print(f"Training Q Player [{self.letter}] for {self.num_episodes} episodes...")
        game_state = game.copy()
        
        for _ in tqdm(range(self.num_episodes)):               
            game_state.restart()
            self.action_history = []
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
    
    def update_rewards(self, reward: float):
        """
        :param reward: reward value at the end of the game
        Given the reward at the end of the game, update the Q-values for each state-action pair in the game with the Bellman equation:
            Q(s, a) = Q(s, a) + alpha * (reward + gamma * max(Q(s', a')) - Q(s, a)) 
                    with each (s, a) stored self.action_history.
        We need to update the Q-values for each state-action pair in the action history because the reward is only received at the end.
          
        """
        ######### YOUR CODE HERE #########
        

        
        ######### YOUR CODE HERE #########

    def choose_action(self, game: TicTacToe) -> Union[List[int], Tuple[int, int]]:
        """
        Choose action with ε-greedy strategy.
        if random number < ε, choose random action
        else choose action with the highest Q-value
        """
        action = None
        ######### YOUR CODE HERE #########
        

        
        ######### YOUR CODE HERE #########                                
        return action
    
    def update_q_values(self, state, action, next_state, reward):
        """
        Given (s, a, s', r), update the Q-value for the state-action pair (s, a) using the Bellman equation:
            Q(s, a) = Q(s, a) + alpha * (reward + gamma * max(Q(s', a')) - Q(s, a))
        """
        ######### YOUR CODE HERE #########
        

        
        ######### YOUR CODE HERE #########  
    
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
        self.epsilon = 0 # No exploration 
        move = self.choose_action(game)
        return move
    
    def __str__(self):
        return "Q-Learning Player"
    