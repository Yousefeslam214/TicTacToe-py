from help_fun import *

class Menu:
    def __init__(self, choice = ""):
        self.choice = ""

    def display_main_menu(self):
        print("Welcome to X-O game!")
        print("1. Start Game")
        print("2. Quit Game")
        self.choice = input("Enter your choice (1 or 2): ")
        if not check_two_symbols(self.choice, "1", "2"):
            print("Invalid input. symbol must be a (1 or 2). Please try again.")
            print()
            return self.display_main_menu() # Recursive call
        else:
            return (self.choice)

    def display_endgame_menu(self):
        print("Game Over!")
        print("1. Restart Game")
        print("2. Quit Game")
        self.choice = input("Enter your choice (1 or 2): ")
        if not check_two_symbols(self.choice, "1", "2"):
            print("Invalid input. symbol must be a (1 or 2). Please try again.")
            print()
            return self.display_main_menu() # Recursive call
        else:
            return (self.choice)
