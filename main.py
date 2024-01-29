from player import Player
from menu import Menu
from help_fun import *


class Game:
    def __init__(self,order = 0,slot = ""):
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.current_player_idx = 0
        self.line = 3
        self.arr = [str(i) for i in range(1,10)]
        self.order = order
        self.slot = slot

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        clear_screen()
        for idx, player in enumerate(self.players, start=1):
            print(f"Player {idx}, enter your details:")
            if idx == 1:
                print("player symbol is X")
            else:
                print("player symbol is O")
            player.choose_name()
            clear_screen()

    def display_board(self):
        for i in range(0,9,3):
            print("|".join((self.arr[i:i + 3])))
            if i < 6:
                print("-" * 5)
        self.order += 1

    def update_board(self):
        if self.check_win() or self.check_draw():
            return  # Stop the recursion if the game is complete
        if self.order % 2 == 0:
            slot_symbol = "X"
            print("X player ", end="")
            print(f"{self.players[0].name}")
        else:
            slot_symbol = "O"
            print("O player ", end="")
            print(f"{self.players[1].name}")
        if self.order == 0:
            self.display_board()
            self.order += 1
        self.slot = input("choose a cell (1-9): ")
        if self.is_valid_input() and self.is_valid_move():
            self.arr[int(self.slot) - 1] = slot_symbol
            self.display_board()
            self.update_board()
        else:
            print("Invalid input or move. Please try again.")
            self.update_board()
        self.order += 1

    def play_game(self):
        while True:
            self.update_board()
            if self.check_win() or self.check_draw():
                clear_screen()
                self.check_winner()
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def check_winner(self):
        if self.check_draw() == True:
            print("No one win")
        else:
            if self.order % 2 == 0:
                # slot_symbol = "X"
                print("winner X player ", end="")
                print(f"{self.players[0].name}")
            else:
                print("winner O player ", end="")
                print(f"{self.players[1].name}")

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combinations:
            if self.arr[combo[0]] == self.arr[combo[1]] == self.arr[combo[2]]:
                return True
        return False

    def restart_game(self):
        self.reset_board()
        self.current_player_idx = 0
        self.play_game()

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.arr)

    def is_valid_input(self):
        return (self.slot).isdigit() and (int(self.slot) < 10  and int(self.slot) > 0)

    def is_valid_move(self):
        return self.arr[int(self.slot) - 1].isdigit()

    def reset_board(self):
        self.arr = [str(i) for i in range(1, 10)]

    def quit_game(self):
        print("Thank you for playing!")

game = Game()
game.start_game()
