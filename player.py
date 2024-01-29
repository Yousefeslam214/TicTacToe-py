from help_fun import *
class Player:
    def __init__(self,name = "",symbol = ""):
        self.name = name
        self.symbol = symbol

    def choose_name(self):
        """fun input name and check it"""
        self.name = input("Enter your name : ")
        if not check(self.name):
            print("Invalid input. Name must be a string. Please try again.")
            return self.choose_name()  # Recursive call
        # return self.name

    # def choose_symbol(self):
    #     """fun input symbol and check it"""
    #     self.symbol = input(f"{self.name}, choose you symbol (\"o\" or \"x\") : ").upper()
    #     if not check_two_symbols(self.symbol, "X", "O"):
    #         print("Invalid input. symbol must be a (\"o\" or \"x\"). Please try again.")
    #         return self.choose_symbol() # Recursive call
