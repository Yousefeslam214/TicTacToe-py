from help_fun import *

class Board:
    def __init__(self,order = 0):
        self.line = 3
        self.arr = [str(i) for i in range(1,10)]
        self.order = order
        
    
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.arr[i:i+3]))
            if i < 6:
                print("-" * 5)
            
        self.order += 1
    
    def update_board(self):
        
        slot = input("which slot you chose")
        if self.order % 2 == 0:
            slot_symbol = "X"
        else:
            slot_symbol = "O"

        
        for i, value in enumerate(self.arr):
            
            if chr(i) == slot:
                self.arr[i] = slot_symbol
        self.display_board()
        self.order += 1
