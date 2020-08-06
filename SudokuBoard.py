import numpy as np
import random
import time


def print_board(board):
    '''
    prints a NxN board in a presentable manner with
    breaks after every 3 columns and a seperator after
    every 3 rows.

    return --> None
    '''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- '*15)

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], ' ', end='')


def find_empty(board):
    '''
    returns the position of an empty element in a board
    empty element is any false value.
    '''
    for row in range(len(board)):
        for col in range(len(board[0])):
            if not board[row][col]:
                return row, col


def is_valid(board, num, row, col):
    '''
    returns True if num can be placed in (row, col) a valid
    sudoku board.
    '''
    if num in board[row]:
        return False

    # Don't use board[:, col] it was significantly slower
    # and removed support for nested list as an input.
    for y in range(len(board[0])):
        if num == board[row][y]:
            return False

    box_row = row//3
    box_col = col//3

    for board_rows in board[box_row*3: box_row*3 + 3]:
        if num in board_rows[box_col*3: box_col*3 + 3]:
            return False

    return True


def sudoku(board):
    """
    Generates a valid sudoku board, takes in an nested list
    of 9X9 nested list of zeros.
    \n
    Input may be a nested list or a numpy array (mutable data-type)
    \n
    DOESN'T return the board, just mutates the contents.
    """

    # this recursive alogrith was made with the help of
    # www.youtube.com/watch?v=lK4N8E6uNr4
    # but i modified it to make a board insted of solving it

    if not find_empty(board):
        return True

    temp = 0
    trys = 0

    row, col = find_empty(board)

    if (row == 8 and col == 8):
        temp = 1

    while not is_valid(board, temp, row, col) and trys <= 200:
        # Why 200? => prob of a num is 0.1, negation of that = 0.9,
        # 1 - (0.9)^200 is nearly 0.9999999 which almost gunrantees if
        # a num is valid then, it will show up at least once.
        temp = random.randint(1, 9)
        trys = trys + 1

    # BackTracking Part
    if trys <= 200:
        board[row][col] = temp
        if sudoku(board):
            return True

        else:
            board[row][col] = 0

    return False


def create_board():
    now = time.time()
    x = np.zeros([9, 9], int)

    while not x[0][0]:
        sudoku(x)

    print_board(x)
    print(f'\nGenerated a Sudoku Board in {(time.time() - now): .4f} seconds')
    return x


if __name__ == "__main__":

    x = create_board()
