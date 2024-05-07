"""
This module contains the GamePlay class which is responsible for running the game between two players.
* You don't need to read/understand the code.
! The code should not be modified. 
"""
import time
from func_timeout import func_timeout, FunctionTimedOut
from typing import Optional
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
        self.curr_game = 0
        self.num_games = num_games
        self.score = {self.x_player: 0, self.o_player: 0}
        self.timeout = timeout
        
        # Check player initialization
        assert (self.x_player.letter == 'X'), "Wrong letter initialization for Player 1!"
        assert (self.o_player.letter == 'O'), "Wrong letter initialization for Player 2"
        
        self.game = game
            
    def switch_players(self):
        self.x_player, self.o_player = self.o_player, self.x_player
        self.x_player.letter = 'X'
        self.o_player.letter = 'O'
        
    def run(self, num_trials: int = 1):
        if self.mode == 'silent':
            self.run_silent_mode(num_trials)
        elif self.mode == 'plain':
            self.run_plain_mode(num_trials)
        else:
            self.run_ui_mode(num_trials)
        return self.score
        
    def run_plain_mode(self):
        self.game.init_board()
        
        move_times = {str(self.x_player): [], str(self.o_player): []}
        evaluation_start_time = time.time()  # Start the overall evaluation timer

        print("-------------------------")
        for self.curr_game in range(1, self.num_games+1):
            print(f"Game {self.curr_game}: {self.x_player} [X] vs {self.o_player} [O]\n")
            num_moves = 0
            game_start_time = time.time()  # Start timing the game
            current_turn = 'X'
            winner = None

            while len(self.game.avail_moves) > 0:
                if current_turn == 'X':
                    self.curr_player = self.x_player
                else:
                    self.curr_player = self.o_player

                move_start_time = time.time()
                
                # Get move from current player. Set timeout for AI agent if specified
                if self.timeout == None or str(self.curr_player) == 'Human Player':
                    try:
                        move = self.curr_player.get_move(self.game)
                    except Exception as e:
                        print(f"Error when running {self.curr_player}: {e}")
                else:
                    try:
                        move = func_timeout(self.timeout, self.curr_player.get_move, args=(self.game,))
                    except FunctionTimedOut:
                        print(f"{self.curr_player} [{self.curr_player.letter}] move timed out!")
                    except Exception as e:
                        print(f"Error when running {self.curr_player}: {e}")
                        
                move_end_time = time.time()

                # Calculate move duration and update move count and runtime
                move_duration = move_end_time - move_start_time
                num_moves += 1
                move_times[str(self.curr_player)].append(move_duration)

                x, y = move[0], move[1]

                # time.sleep(.4) # Slow down the game
                if self.game.set_move(x, y, self.curr_player.letter):
                    self.game.print_board()
                    print(f"[{move_duration:.2f}s] {str(self.curr_player)} [{self.curr_player.letter}] makes a move to square {tuple(move)}")

                    if self.game.wins(self.curr_player.letter):
                        winner = self.curr_player
                        break

                    current_turn = 'X' if current_turn == 'O' else 'O'
                else:
                    raise RuntimeError("The selected move is invalid. There is a bug in the code!")

            game_end_time = time.time()  # End timing the game
            game_duration = game_end_time - game_start_time
            print(f"Game {self.curr_game} duration: {game_duration:.2f} seconds")

            if winner:
                print(f"{winner} wins in {(num_moves+1)//2} moves!")
                self.score[str(winner)] += 1
            else:
                print("It's a draw!")
            print("-------------------------")

            # Restart the game and alternate players
            self.game.restart()
            self.switch_players()
            winner = None  # Reset winner for the next game

        evaluation_end_time = time.time()  # End the overall evaluation timer
        total_evaluation_time = evaluation_end_time - evaluation_start_time

        # Print final scores and time statistics
        print("\nFinal Scoreboard:")
        for player, wins in self.score.items():
            print(f"{player} wins {wins}/{self.num_games} games")
        for player, times in move_times.items():
            avg_time_per_move = sum(times) / len(times) if times else 0
            print(f"{player} average move duration: {avg_time_per_move:.2f} seconds")

        print(f"Total evaluation time: {total_evaluation_time:.2f} seconds")
        
    def run_silent_mode(self):
        move_times = {str(self.x_player): [], str(self.o_player): []}
        evaluation_start_time = time.time()  # Start the overall evaluation timer

        print("-------------------------")
        for self.curr_game in range(1, self.num_games + 1):
            num_moves = 0
            game_start_time = time.time()  # Start timing the game
            current_turn = 'X'
            winner = None

            while len(self.game.avail_moves) > 0:
                if current_turn == 'X':
                    self.curr_player = self.x_player
                else:
                    self.curr_player = self.o_player

                move_start_time = time.time()
                
                # Get move from current player. Set timeout for AI agent if specified
                if self.timeout == None or str(self.curr_player) == 'Human Player':
                    try:
                        move = self.curr_player.get_move(self.game)
                    except Exception as e:
                        print(f"Error when running {self.curr_player}: {e}")
                else:
                    try:
                        move = func_timeout(self.timeout, self.curr_player.get_move, args=(self.game,))
                    except FunctionTimedOut:
                        print(f"{self.curr_player} [{self.curr_player.letter}] move timed out!")
                    except Exception as e:
                        print(f"Error when running {self.curr_player}: {e}")
                        
                move_end_time = time.time()

                # Calculate move duration and update move count and runtime
                move_duration = move_end_time - move_start_time
                num_moves += 1
                move_times[str(self.curr_player)].append(move_duration)

                x, y = move[0], move[1]

                # time.sleep(.4) # Slow down the game
                if self.game.set_move(x, y, self.curr_player.letter):
                    self.update_board(self.curr_player, move)
                    print(f"[{move_duration:.2f}s] {str(self.curr_player)} [{self.curr_player.letter}] makes a move to square {tuple(move)}")

                    if self.game.wins(self.curr_player.letter):
                        winner = self.curr_player
                        break

                    current_turn = 'X' if current_turn == 'O' else 'O'
                else:
                    raise RuntimeError("The selected move is invalid. There is a bug in the code!")

            game_end_time = time.time()  # End timing the game
            game_duration = game_end_time - game_start_time
            print(f"Game {self.num_games} duration: {game_duration:.2f} seconds")

            if winner:
                print(f"{winner} wins in {(num_moves+1)//2} moves!")
                self.score[str(winner)] += 1
            else:
                print("It's a draw!")
            print("-------------------------")

            # Restart the game and alternate players
            self.game.restart()
            self.x_player, self.o_player = self.o_player, self.x_player
            winner = None  # Reset winner for the next game

        evaluation_end_time = time.time()  # End the overall evaluation timer
        total_evaluation_time = evaluation_end_time - evaluation_start_time

        # Print final scores and time statistics
        print("\nFinal Scoreboard:")
        for player, wins in self.score.items():
            print(f"{player} wins {wins}/{self.num_games} games")
        for player, times in move_times.items():
            avg_time_per_move = sum(times) / len(times) if times else 0
            print(f"{player} average move duration: {avg_time_per_move:.2f} seconds")

        print(f"Total evaluation time: {total_evaluation_time:.2f} seconds")
    
    def run_ui_mode(self):
        self.ui = GameRender(game=self.game)
        self.ui.mainloop()
        
        time.sleep(.5) # Wait for the UI to load
        self.curr_player = self.x_player # X Player starts first
        self.ui.update_display(f"{self.curr_player} [{self.curr_player.letter}]'s turn", color="blue" if self.curr_player.letter == "X" else "green")
        
        if str(self.x_player) != 'Human Player':
            self.ai_turn()
        
    # Following functions only run in UI mode
    def human_turn(self, x, y):
        self._process_move(x, y)
        self.ai_turn()
        
    def ai_turn(self):
        if self.timeout == None:
            try:
                move = self.curr_player.get_move(self.game)
            except Exception as e:
                print(f"Error when running {self.curr_player}: {e}")
        else:
            try:
                move = func_timeout(self.timeout, self.curr_player.get_move, args=(self.game,))
            except FunctionTimedOut:
                print(f"{self.curr_player} [{self.curr_player.letter}] move timed out!")
            except Exception as e:
                print(f"Error when running {self.curr_player}: {e}")
        
        self._process_move(move[0], move[1])
    
    def _process_move(self, x, y):
        if self.game.set_move(x, y, self.curr_player.letter):
            print(f"{str(self.curr_player)} [{self.curr_player.letter}] makes a move to square {(x, y)}")
            self.ui.update_board(self.curr_player, (x, y))
        else:
            raise RuntimeError("The selected move is invalid. There is a bug in the code!")
        
        if self.game.wins(self.curr_player.letter):
            self.score[str(winner)] += 1
            winner = self.curr_player
            print(f"{winner} wins")
            self.ui.update_display(f"{self.curr_player} wins", color="blue" if self.curr_player.letter == "X" else "blue")
            self.ui.highlight_cells(self.game.winner_combos)
            self.ui.update_scoreboard()
            if self.curr_game < self.num_games:
                self._restart_game()
            else:
                self._finish()
        elif len(self.game.avail_moves) == 0:
            print("It's a draw")
            self.ui.update_display("It's a draw", color="black")
            self.ui.update_scoreboard()
            if self.curr_game < self.num_games:
                self._restart_game()
            else:
                self._finish()
        else:
            self.curr_player = self.o_player if self.curr_player == self.x_player else self.x_player
            self.ui.update_display(f"{self.curr_player} [{self.curr_player.letter}]'s turn", color="blue" if self.curr_player.letter == "X" else "green")
        
    def _restart_game(self):
        self.switch_players()
        self.game.restart()
        self.ui.reset_board()
        self.curr_game += 1
        self.curr_player = None
    
    def _finish(self):
        print("\nFinal Scoreboard:")
        for player, wins in self.score.items():
            print(f"{player} wins {wins}/{self.num_games} games")
        time.sleep(5)
        self.ui.destroy()
        
############################################################################################################
#*  The code below is used for visualization of the game. It is not required for the core functionality.  *#
import tkinter as tk
from tkinter import font

class GameRender(tk.Tk):
    def __init__(self, gameplay: GamePlay):
        super().__init__()
        self.title(str(self.gameplay.game))
        self.gameplay = gameplay
        self.cells = dict()
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()
        self.update_scoreboard(self.gameplay.score)

    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def _create_board_display(self):
        score_frame = tk.Frame(self, bd=3, relief="groove", padx=10, pady=10)
        score_frame.pack(side="right", fill="both", expand=True)

        # Scoreboard title label
        scoreboard_title = tk.Label(score_frame, 
                                    font=('Segoe UI', 25, 'bold'), 
                                    text="Scoreboard", 
                                    )
        scoreboard_title.pack(side="top", fill="x")

        # Scoreboard label
        score_label = tk.Label(score_frame, 
                                    font=('Segoe UI', 20, 'bold'),
                                    justify=tk.LEFT
                                    )
        score_label.pack(side="top", fill="x", expand=True)
        
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack(side="top", fill="x")
        
    def _create_board_grid(self):
        game = str(self.gameplay.game)
        if game == 'Tic Tac Toe':
            self._create_ttt_board()
        elif game == 'Gomoku':
            self._create_gmk_board()
        else:
            raise ValueError("Invalid game type")
    
    def _create_ttt_board(self):
        self.turn_label = tk.Label(
            master=self,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.turn_label.pack()
        
        board_frame = tk.Frame(master=self)
        board_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                human_turn = lambda x=row, y=col: self.gameplay.human_turn(x, y)
                button = tk.Button(
                    master=board_frame,
                    font=('Segoe UI', 25, 'bold'),
                    width=3, height=2, fg="black",
                    highlightbackground="lightblue",
                    func=human_turn,
                )
                self.cells[button] = (row, col)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
    def _create_gmk_board(self):
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
                                   font=('Segoe UI', 20, 'bold'), 
                                   pady=5)
        self.turn_label.pack(side="top", fill="x")

        # Board frame setup
        board_frame = tk.Frame(self)
        board_frame.pack(side="left")

        # Create grid buttons
        size = self.gameplay.game.size
        for row in range(size):
            board_frame.rowconfigure(row, weight=1, minsize=2, pad=0)
            board_frame.columnconfigure(row, weight=1, minsize=2, pad=0)
            for col in range(size):
                human_turn = lambda x=row, y=col: self.gameplay.human_turn(x, y)
                button = tk.Button(
                    master=board_frame, 
                    font=('Segoe UI', 15),
                    height=2, width=2, fg="black",
                    borderwidth=0, highlightthickness=0, func=human_turn
                )
                self.cells[(row, col)] = button
                button.grid(row=row, column=col, sticky="nsew")
                
    def update_board(self, letter, x, y):
        self.cells[(x,y)].config(text=letter)
        self.cells[(x,y)].config(fg="blue" if letter == "X" else "green")

    def update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def highlight_cells(self, winner_combos):
        for move in winner_combos:
            self.cells[move].config(highlightbackground="red")
    
    def update_scoreboard(self):
        scoreboard = self.gameplay.score
        player_1, player_2 = scoreboard.keys()
        display_score = f"{player_1}: {scoreboard[player_1]}\n\n{player_2}: {scoreboard[player_2]}"
        self.score_label.config(text=display_score)
        
    def reset_board(self):
        self._game.reset_game()
        self._update_display(msg="Ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")
        
    def disable_buttons(self):
        for button in self.cells:
            button.config(state=tk.DISABLED) 
    
    def enable_buttons(self):
        for button in self.cells:
            if self.cells[button] in self.gameplay.game.avail_moves:   
                button.config(state=tk.NORMAL)
 