"""
This module is made by studentA
"""
import random

def is_player_starting():
    """
    This function checks if the player is starting
    """
    coin = input('Choose H (heads) or T (tails): ')
    rand_coin = random.choice(['H', 'T'])
    if coin == rand_coin:
        print('You\'re starting!')
        return True

    print('The computer is starting!')
    return False


def get_user_move(board):
    """
    This function gets the user move
    """
    choice = input('Choose a cell: ')

    cell_1 = choice[0]
    cell_2 = choice[1]
    if cell_1.isnumeric():
        num = cell_1
        letter = cell_2
    else:
        num = cell_2
        letter = cell_1
    col = 0
    if letter == 'A':
        col = 0
    elif letter == 'B':
        col = 1
    elif letter == 'C':
        col = 2
    elif letter == 'D':
        col = 3
    elif letter == 'E':
        col = 4

    board[int(num)][col] = 'O'
    return board


def ai_move(board):
    """
    This function makes a move for the AI
    """
    y, x = random.randint(0, 4), random.randint(0, 4)
    counter = 0
    while board[y][x] != ' ' and counter < 15:
        y, x = random.randint(0, 4), random.randint(0, 4)
        counter += 1
    board[y][x] = 'X'
    return board
