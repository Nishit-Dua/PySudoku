import random
import time
import numpy as np
from SudokuBoard import print_board, create_board, is_valid, find_empty


def make_puzzle(board, holes_factor=5):
    '''
    Creates holes (zeros) in the sudoku board.
    returns mutated board.
    '''
    hole_multiple = 6  # Higher this more holes are created

    shape = board.shape
    length = board.size

    board = board.flatten()  # I am using numpy, define a flatten Func\
    # if you plan to use nessted lists

    holes = holes_factor*hole_multiple
    for i in range(holes):
        board[random.randint(0, length - 1)] = 0

    n_zeros = np.count_nonzero(board == 0)
    print(f'generated {n_zeros} holes')
    return board.reshape(shape)


def solve(puzzle):
    '''
    Solved the 'Holed' sudoku recursively using backtracking
    doesn't Return the Final Result insted mutates the puzzle
    '''

    if not find_empty(puzzle):
        return True
    row, col = find_empty(puzzle)

    for i in range(1, 10):
        if is_valid(puzzle, i, row, col):
            puzzle[row][col] = i

            if(solve(puzzle)):
                return True

            else:
                puzzle[row][col] = 0

    return False


if __name__ == "__main__":
    x = create_board()
    print('\n', '!-! '*8, '\n')

    print('Creating holes into board...\n')
    try:
        hole_factor = int(input('Difficulty of the puzze (1-10): '))
    except ValueError:
        print('Got a Value Error Defaulting to 5')
        hole_factor = 5
    print()

    now = time.time()
    x = make_puzzle(x, holes_factor=hole_factor)
    print_board(x)

    print('\nsolving the puzzle....\n')
    solve(x)
    print_board(x)

    print(f'\ncreated and Solved puzzle in {(time.time() - now):.4f} seconds.')
