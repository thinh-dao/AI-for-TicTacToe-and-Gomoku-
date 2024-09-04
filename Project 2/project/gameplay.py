"""
This module contains the GamePlay class which is responsible for running the game between two players.
* You don't need to read/understand the code.
! The code should not be modified. 
"""
import time
import threading
from func_timeout import func_timeout, FunctionTimedOut
from typing import Optional
import random
from .player import Player
from .game import Game

class GamePlay():
    def __init__(self, x_player: Player, o_player: Player, game: Game , mode: str = "plain", num_games: int = 1, timeout: Optional[int] = None):
        """
        Three modes for visualization of the game:
        1. "silent": game play is not shown (Not available for Human Player)
        2. "plain": game play is shown in terminal
        3. "ui": game play is shown with GUI       
        """
        self.x_player = x_player
        self.o_player = o_player
        self.mode = mode
        self.curr_player = None
        self.curr_game = 1
        self.num_games = num_games
        self.score = {self.x_player: 0, self.o_player: 0}
        self.timeout = timeout
        
        if str(self.x_player) == 'Human Player' or str(self.o_player) == 'Human Player':
            self.delay = 0
        else:
            self.delay = 400
            
        # Check player initialization
        assert (self.x_player.letter == 'X'), "Wrong letter initialization for Player 1!"
        assert (self.o_player.letter == 'O'), "Wrong letter initialization for Player 2"
        
        self.game = game
            
    def switch_players(self):
        self.x_player, self.o_player = self.o_player, self.x_player
        self.x_player.letter = 'X'
        self.o_player.letter = 'O'
        if hasattr(self.x_player, 'restart') and callable(getattr(self.x_player, 'restart')):
            self.x_player.restart()
        if hasattr(self.o_player, 'restart') and callable(getattr(self.o_player, 'restart')):
            self.o_player.restart()
        
    def run(self):
        if self.mode == 'ui':
            self.run_ui_mode()
        else:
            self.run_plain_mode()
        return self.score
        
    def run_plain_mode(self):    
        move_times = {str(self.x_player): [], str(self.o_player): []}
        evaluation_start_time = time.time()  # Start the overall evaluation timer

        print("--------------------------------------------------")
        for self.curr_game in range(1, self.num_games+1):
            if self.mode != 'silent': 
                print(f"Game {self.curr_game}: {self.x_player} [X] vs {self.o_player} [O]")
                self.game.init_board()
                self.game.print_board()
            
            num_moves = 0
            game_start_time = time.time()  # Start timing the game
            current_turn = 'X'
            winner = None

            while len(self.game.empty_cells()) > 0:
                if current_turn == 'X':
                    self.curr_player = self.x_player
                else:
                    self.curr_player = self.o_player

                move_start_time = time.time()
                
                # Get move from current player. Set timeout for AI agent if specified
                if self.timeout == None or str(self.curr_player) == 'Human Player':
                    move = self.curr_player.get_move(self.game.copy())
                else:
                    try:
                        move = func_timeout(self.timeout, self.curr_player.get_move, args=(self.game,))
                    except FunctionTimedOut:
                        print(f"{self.curr_player} [{self.curr_player.letter}] move timed out! Taking random step.")
                        # Take random move
                        move = random.choice(self.game.empty_cells())
                        
                move_end_time = time.time()

                # Calculate move duration and update move count and runtime
                move_duration = move_end_time - move_start_time
                num_moves += 1
                move_times[str(self.curr_player)].append(move_duration)

                x, y = move[0], move[1]

                if self.game.set_move(x, y, self.curr_player.letter):
                    if self.mode != 'silent':
                        self.game.print_board()
                        print(f"{str(self.curr_player)} [{self.curr_player.letter}] makes a move to square {tuple(move)} [{move_duration:.2f}s]")

                    if self.game.wins(self.curr_player.letter):
                        winner = self.curr_player
                        break

                    current_turn = 'X' if current_turn == 'O' else 'O'
                else:
                    print(f"The selected move {(x, y)} from {self.curr_player} is invalid. Maybe there is a bug in the code! Taking random move instead.")
                    move = random.choice(self.game.empty_cells())
                    x, y = move[0], move[1]
                    self.game.set_move(x, y, self.curr_player.letter)

            game_end_time = time.time()  # End timing the game
            game_duration = game_end_time - game_start_time

            if winner:
                print(f"Game {self.curr_game} result: {winner} wins in {(num_moves+1)//2} moves!")
                self.score[winner] += 1
            else:
                print(f"Game {self.curr_game} result: Draw!")
            
            if self.mode != 'silent': 
                print(f"Game {self.curr_game} duration: {game_duration:.2f} seconds")
            print("--------------------------------------------------")

            # Restart the game and alternate players
            self.game.restart()
            self.switch_players()
            winner = None  # Reset winner for the next game

        evaluation_end_time = time.time()  # End the overall evaluation timer
        total_evaluation_time = evaluation_end_time - evaluation_start_time

        # Print final scores and time statistics
        print("Final Scoreboard:")
        for player, wins in self.score.items():
            print(f"{player} wins {wins}/{self.num_games} games")
        
        draw = self.num_games - sum(self.score.values())
        print(f"Draws {draw}/{self.num_games} games\n")
        
        for player, times in move_times.items():
            avg_time_per_move = sum(times) / len(times) if times else 0
            print(f"{player} average move duration: {avg_time_per_move:.2f} seconds")

        print(f"Total evaluation time: {total_evaluation_time:.2f} seconds\n")
    
    def run_ui_mode(self):
        self.ui = GameRender(gameplay=self)
        
        self.curr_player = self.x_player # X Player starts first
        self.ui.update_display(f"[{self.curr_player.letter}] {self.curr_player}'s turn", color="blue" if self.curr_player.letter == "X" else "green")
        
        if str(self.x_player) != 'Human Player':
            self.ui.after(200, lambda: self.ai_turn())
            
        self.ui.mainloop()
        
    def ai_turn(self):
        def ai_move():
            if self.timeout is None:
                move = self.curr_player.get_move(self.game.copy())
            else:
                try:
                    move = func_timeout(self.timeout, self.curr_player.get_move, args=(self.game,))
                except FunctionTimedOut:
                    print(f"{self.curr_player} [{self.curr_player.letter}] move timed out! Taking random step.")
                    move = random.choice(self.game.empty_cells())
            
            self.ui.after(self.delay, self._process_move(move[0], move[1]))

        # Run the AI move calculation in a separate thread
        ai_thread = threading.Thread(target=ai_move)
        ai_thread.start()
    
    def _process_move(self, x, y):
        if self.game.set_move(x, y, self.curr_player.letter):
            print(f"{str(self.curr_player)} [{self.curr_player.letter}] makes a move to square {(x, y)}")
            self.ui.update_board(self.curr_player.letter, x, y)
        else:
            print(f"The selected move {(x, y)} from {self.curr_player} is invalid. Maybe there is a bug in the code! Taking random move instead.")
            move = random.choice(self.game.empty_cells())
            x, y = move[0], move[1]
            self.ui.update_board(self.curr_player.letter, x, y)
        if self.game.wins(self.curr_player.letter):
            winner = self.curr_player
            self.score[winner] += 1
            print(f"Game {self.curr_game} result: {winner} wins!")
            print("--------------------------------------------------")
            self.ui.update_display(f"{self.curr_player} wins", color="blue" if self.curr_player.letter == "X" else "green")
            self.ui.highlight_cells(self.game.win_combo)
            self.ui.disable_buttons()
            self.ui.update_scoreboard()
            
            # Delay before restarting or finishing the game
            self.ui.after(1000, self._check_game_continuation)
        elif len(self.game.empty_cells()) == 0:
            print(f"Game {self.curr_game} result: Draw!")
            print("--------------------------------------------------")
            self.ui.update_display("It's a draw", color="black")
            self.ui.update_scoreboard()
            
            # Delay before restarting or finishing the game
            self.ui.after(1000, self._check_game_continuation)
        else:
            self.curr_player = self.o_player if self.curr_player == self.x_player else self.x_player
            self.ui.update_display(f"[{self.curr_player.letter}] {self.curr_player}'s turn", color="blue" if self.curr_player.letter == "X" else "green")
            if str(self.curr_player) != 'Human Player':
                self.ai_turn()

    def _check_game_continuation(self):
        """Check if the game should continue or end."""
        if self.curr_game < self.num_games:
            self._restart_game()
        else:
            self._finish()
        
    def _restart_game(self):
        self.switch_players()
        self.game.restart()
        self.ui.reset_board()
        self.curr_game += 1
        
        self.curr_player = self.x_player # X Player starts first
        self.ui.update_display(f"[{self.curr_player.letter}] {self.curr_player}'s turn", color="blue" if self.curr_player.letter == "X" else "green")
        
        if str(self.x_player) != 'Human Player':
            self.ui.after(200, lambda: self.ai_turn())
        
    def _finish(self):
        self.ui.disable_buttons()
        print("\nFinal Scoreboard:")
        for player, wins in self.score.items():
            print(f"{player} wins {wins}/{self.num_games} games")
        draw = self.num_games - sum(self.score.values())
        print(f"Draws {draw}/{self.num_games} games\n")
        
############################################################################################################
#*  The code below is used for visualization of the game. It is not required for the core functionality.  *#
import tkinter as tk
from tkinter import font

class GameRender(tk.Tk):
    def __init__(self, gameplay: GamePlay):
        super().__init__()
        self.title(str(gameplay.game))
        self.gameplay = gameplay
        self.cells = dict()
        self._create_board_display()
        self._create_board_grid()
        self.update_scoreboard()

    def _create_board_display(self):
                # Scoreboard frame setup
        score_frame = tk.Frame(self, bd=3, relief="groove", padx=10, pady=10)
        score_frame.pack(side="right", fill="both", expand=True)

        # Scoreboard title label
        scoreboard_title = tk.Label(score_frame, 
                                    font=('Segoe UI', 25, 'bold'), 
                                    text="Scoreboard", 
                                    )
        scoreboard_title.pack(side="top", fill="x")

        # Scoreboard label
        self.score_label = tk.Label(score_frame, 
                                    font=('Segoe UI', 20, 'bold'),
                                    justify=tk.LEFT
                                    )
        self.score_label.pack(side="top", fill="x", expand=True)

        # Turn label above the board frame
        self.turn_label = tk.Label(self, 
                                   text=f"Ready?", 
                                   font=('Segoe UI', 30, 'bold'), 
                                   pady=5)
        self.turn_label.pack(side="top", fill="x")
        
    def _create_board_grid(self):
        game = str(self.gameplay.game)
        if game == 'Tic Tac Toe':
            self._create_ttt_board()
        elif game == 'Gomoku':
            self._create_gmk_board()
        else:
            raise ValueError("Invalid game type")
    
    def _create_ttt_board(self):
        board_frame = tk.Frame(master=self)
        board_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                human_turn = lambda x=row, y=col: self.gameplay._process_move(x, y)
                button = tk.Button(
                    master=board_frame,
                    font=('Segoe UI', 35, 'bold'),
                    width=6, height=4, fg="black", highlightbackground="lightblue",
                    padx=0, pady=0,
                    command=human_turn,
                )
                self.cells[(row, col)] = button
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
    def _create_gmk_board(self):
        # Board frame setup
        board_frame = tk.Frame(self)
        board_frame.pack(side="left")

        # Create grid buttons
        size = self.gameplay.game.size
        for row in range(size):
            board_frame.rowconfigure(row, weight=1, minsize=2, pad=0)
            board_frame.columnconfigure(row, weight=1, minsize=2, pad=0)
            for col in range(size):
                human_turn = lambda x=row, y=col: self.gameplay._process_move(x, y)
                button = tk.Button(
                    master=board_frame, 
                    font=('Segoe UI', 15),
                    height=2, width=2, fg="black",
                    borderwidth=0, highlightthickness=0, highlightbackground="lightblue",
                    padx=0, pady=0,
                    command=human_turn,
                )
                self.cells[(row, col)] = button
                button.grid(row=row, column=col, sticky="nsew")
                
    def update_board(self, letter, x, y):
        self.cells[(x,y)].config(text=letter)
        self.cells[(x,y)].config(fg="blue" if letter == "X" else "green")

    def update_display(self, msg, color="black"):
        self.turn_label["text"] = msg
        self.turn_label["fg"] = color

    def highlight_cells(self, win_combo):
        for move in win_combo:
            self.cells[move].config(highlightbackground="red")
    
    def update_scoreboard(self):
        scoreboard = self.gameplay.score
        player_1, player_2 = scoreboard.keys()
        display_score = f"{player_1}: {scoreboard[player_1]}\n\n{player_2}: {scoreboard[player_2]}"
        self.score_label.config(text=display_score)
        
    def reset_board(self):
        self.update_display(msg="Ready?")
        for button in self.cells.keys():
            self.cells[button].config(text="")
            self.cells[button].config(highlightbackground="lightblue")
            self.cells[button].config(fg="black")
            self.cells[button].config(state=tk.NORMAL)
        
    def disable_buttons(self):
        for button in self.cells:
            self.cells[button].config(state=tk.DISABLED) 
    
    def enable_buttons(self):
        for button in self.cells:
            if button in self.gameplay.game.empty_cells():   
                self.cells[button].config(state=tk.NORMAL)
 