"""
This module is main module.
"""

from student_a import new_board, announce_outcome, print_board, is_game_over
from student_b import ai_move, get_user_move, is_player_starting

if __name__ == '__main__':
    board = new_board()
    PLAYERS_MOVE = is_player_starting()
    while not is_game_over(board):
        print_board(board)
        board = PLAYERS_MOVE and get_user_move(board) or ai_move(board)
        PLAYERS_MOVE = not PLAYERS_MOVE

    announce_outcome(board)
