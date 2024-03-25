import random
import tkinter as tk

class DiceRollGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Rolling Game")
        self.geometry("400x350")
        self.max_score = 50
        self.current_player = 0
        self.player_scores = []
        self.player_names = []

        self.create_widgets()

    def create_widgets(self):
        # Number of Players
        self.players_label = tk.Label(self, text="Enter the number of players (2-4):")
        self.players_label.grid(row=0, column=0, pady=5, padx=5)

        self.players_entry = tk.Entry(self)
        self.players_entry.grid(row=0, column=1, pady=5, padx=5)

        # Player Names
        self.name_label = tk.Label(self, text="Enter player names separated by commas:")
        self.name_label.grid(row=1, column=0, pady=5, padx=5)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, pady=5, padx=5)

        # Start Game Button
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

        # Roll Dice Button
        self.roll_button = tk.Button(self, text="Roll Dice", command=self.roll_dice, state=tk.DISABLED)
        self.roll_button.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

        # End Game Button
        self.end_button = tk.Button(self, text="End Game", command=self.end_game, state=tk.DISABLED)
        self.end_button.grid(row=4, column=0, columnspan=2, pady=5, padx=5)

        # Result Label
        self.result_label = tk.Label(self, text="", font=("Arial", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10, padx=5)

    def start_game(self):
        num_players = self.players_entry.get()
        try:
            num_players = int(num_players)
            if num_players < 2 or num_players > 4:
                raise ValueError
        except ValueError:
            self.result_label.config(text="Invalid number of players. Must be between 2 and 4.", fg="red")
            return

        player_names = self.name_entry.get().split(',')
        if len(player_names) != num_players:
            self.result_label.config(text="Please enter names for all players.", fg="red")
            return

        self.player_scores = [0] * num_players
        self.player_names = player_names
        self.current_player = 0

        self.result_label.config(text=f"{self.player_names[self.current_player]}'s turn: Roll the dice!", fg="blue")
        self.roll_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.end_button.config(state=tk.NORMAL)

    def roll_dice(self):
        roll_value = random.randint(1, 6)
        if roll_value == 1:
            self.result_label.config(text="You rolled a 1! Turn done!", fg="red")
        else:
            self.player_scores[self.current_player] += roll_value
            self.result_label.config(text=f"You rolled a {roll_value}. Your score for this turn is: {roll_value}", fg="green")
            self.result_label.after(1500, self.update_score)

    def update_score(self):
        self.result_label.config(text=f"Total score for {self.player_names[self.current_player]}: {self.player_scores[self.current_player]}", fg="black")
        if self.player_scores[self.current_player] >= self.max_score:
            self.result_label.config(text=f"Player {self.player_names[self.current_player]} wins with a score of {self.player_scores[self.current_player]}!", fg="blue")
            self.roll_button.config(state=tk.DISABLED)
            self.end_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)
        else:
            self.current_player = (self.current_player + 1) % len(self.player_names)
            self.result_label.config(text=f"{self.player_names[self.current_player]}'s turn: Roll the dice!", fg="blue")

    def end_game(self):
        self.roll_button.config(state=tk.DISABLED)
        self.end_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.result_label.config(text="Game ended. Click 'Start Game' to play again.", fg="black")

if __name__ == "__main__":
    game = DiceRollGame()
    game.mainloop()
