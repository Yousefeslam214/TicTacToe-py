import os

def check(name):
    """
    this function used to check if input have number or not
    name : is the input
    """
    return all(map(
        lambda char: 65 <= ord(char) <= 90 or
        97 <= ord(char) <= 122, name)) and name

def check_two_symbols(name, x, y):
    """this fun input symbol and check if symbol true of not"""
    return (name != "") and (name == x or name == y)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
