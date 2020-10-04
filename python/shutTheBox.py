import random

def start_game():
    while len(box_numbers) > 1
        print("Shut the Box!")
        print_box_numbers()
        roll_dice()
        get_input()
        

box_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_input():
    selection = input("type a number ")
    selection = int(selection)
    print(selection)

"""
def check_valid_input(selectionx):
    for i in box_numbers:
        if i == 
"""

def print_box_numbers():
    print(box_numbers)
 
def roll_dice():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    dice_sum = dice1 + dice2
    print(dice1, dice2)
    print("SUM: " + str(dice_sum))

start_game()


