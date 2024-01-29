from player import Player
from menu import Menu
from help_fun import *

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Game:
    def __init__(self,order = 0,slot = ""):
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.current_player_idx = 0
        self.line = 3
        self.arr = [str(i) for i in range(1,10)]
        self.order = order
        self.slot = slot

    def display_board(self,):
        for i in range(0,9,3):
            print("|".join((self.arr[i:i + 3])))
            if i < 6:
                print("-" * 5)
        self.order += 1

    def update_board(self):
        self.Game.check_win()
        # for i in self.arr:
        #     if 
        if self.order % 2 == 0:
            slot_symbol = "X"
            print("X play")
        else:
            slot_symbol = "O"
            print("O play")
        self.slot = input("which slot you chose : ")
        if self.is_valid_input():
            if self.is_valid_move():
                self.arr[int(self.slot) - 1] = slot_symbol
                self.display_board()
                self.update_board()
            else:
                print("invvvaled------")
                self.update_board()
                
        else:
            print("invvvaled------")
            self.update_board()
        self.order += 1

    def is_valid_input(self):
        return (self.slot).isdigit() and (int(self.slot) < 10  and int(self.slot) > 0)

    def is_valid_move(self):
        return self.arr[int(self.slot) - 1].isdigit()

    def reset_board(self):
        self.arr = [str(i) for i in range(1, 10)]




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
            player.choose_name()

            clear_screen()

    def quit_game(self):
        print("Thank you for playing!")

    def play_game(self):
        while True:
            self.update_board()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    # def play_turn(self):
    #     player = self.players[self.current_player_idx]
    #     self.board.display_board()
    #     print(f"{player.name}'s turn ({player.symbol})")
    #     while True:
    #         try:
    #             cell_choisce = int(input("choose a cell (1-9): "))
    #             print(type(cell_choisce))
    #             print(self.board.update_board() == True)
    #             if 1 <= cell_choisce <=9 and self.board.update_board():
    #                 print("yousef")
    #                 break
    #             else:
    #                 print("Invalid move, try again. ")
    #         except ValueError:
    #             print("Please enter a number between 1 and 9.")
    #     self.switch_player()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # colums
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]
    
        for combo in win_combinations:
            if(self.board.arr[combo[0]] == self.board.arr[1] == self.board.arr[combo[2]]):
                return True
            return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.arr)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_idx = 0
        self.play_game()

    def switch_player(self):
        self.current_player_idx = 1 - self.current_player_idx

game = Game()
game.start_game()
