"""
This module is made by studentA
"""

def new_board():
    """
    This function creates a new board
    """
    return [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ',' '],
            [' ', ' ', ' ',' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]

def print_board(board):
    """
    This function prints the board
    """
    print(' -A-B-C-D-E')
    i = 0
    for row in board:
        print(f'{i}|{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|')
        print('------------')
        i += 1

def is_game_over(board):
    """
    This function checks if the game is over
    """
    who_won = ' '
    for row in board:
        if row[0] == row[1] == row[2] == row[3] == row[4] and row[0] != ' ':
            who_won = row[0]
    for i in range(5):
        if (board[0][i] == board[1][i] == board[2][i] == board[3][i]==board[4][i]
                and board[0][i] != ' '):
            who_won = board[0][i]
    if (board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]
            and board[0][0] != ' '):
        who_won = board[0][0]

    if (board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]
            and board[0][4] != ' '):
        who_won = board[0][4]

    if all(cell != ' ' for row in board for cell in row):
        who_won = 'D'

    if who_won == ' ':
        return False

    return who_won

def announce_outcome(board):
    """
    this function tells who win
    """
    print_board(board)
    who_won = is_game_over(board)
    if who_won == 'X':
        print("AI won!")
    elif who_won == 'O':
        print("You won!")
    else:
        print('It\'s a tie!')
