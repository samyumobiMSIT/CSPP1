"""
Program to solve sudoku from input file.
"""
import sys
import time
import numpy as np


def read_input(filename):
    """Take file name and return 2d array = board"""
    with open(str(filename), 'r') as file:
        board = np.array([line.split() for line in file]).astype(int)
    return board


def print_board(board):
    """Take 2d array board and print"""
    for i in range(len(board)):
        for j in range(len(board[:])):
            print(str(board[i, j]) + " ", end='')
            # print(str(type(board[i,j])) + " ",end='' )
        print()


def naive_solver(board):
    """Naive approach to solving sudoku board"""
    cell_counter = 1  # cell counter
    init_board = np.copy(board)  # make copy of initial board
    forward = 1  # keep track of direction moving on board

    # main solving loop
    while cell_counter > 0 and cell_counter < 82:
        # case 1: original cell was empty and 9 hasn't been tested
        # print(int((cell_counter-1)/9), (cell_counter-1)%9)
        if (init_board[int((cell_counter - 1) / 9), (cell_counter - 1) % 9] == 0 and
                board[int((cell_counter - 1) / 9), (cell_counter - 1) % 9] < 9):
            # print('case1 ' + str(cell_counter))
            forward = 1
            board[int((cell_counter - 1) / 9), (cell_counter - 1) % 9] += 1
            if not any_duplicates(board):
                cell_counter += 1
        # case 2: original cell was empty, but have tried all numbers
        elif (init_board[int((cell_counter - 1) / 9), (cell_counter - 1) % 9] == 0):
            board[int((cell_counter - 1) / 9), (cell_counter - 1) % 9] = 0
            # print('case2 ' + str(cell_counter))
            cell_counter -= 1
            forward = -1
        # case 3: cell was filled to start
        else:
            # print('case3 ' + str(cell_counter))
            if forward == 1:
                cell_counter += 1
            else:
                cell_counter -= 1

    # Check if solution or not
    if cell_counter == 0:
        raise ValueError("Board has no solution")


def any_duplicates(board):
    """Check all rows, columns, and 9x9 squares for duplicates."""
    # Check all value
    for num in range(1, 10):
        # Check rows and column
        for i in range(0, 9):
            row_val_count = len(list(map(str, np.where(board[:, i] == num)[0])))
            col_val_count = len(list(map(str, np.where(board[i, :] == num)[0])))
            if row_val_count > 1 or col_val_count > 1:
                return True
        # Check boxes of 9
        box_val_count = []
        box_val_count.append(len(list(map(str, np.where(board[0:3, 0:3] == num)[0]))))
        box_val_count.append(len(list(map(str, np.where(board[0:3, 3:6] == num)[0]))))
        box_val_count.append(len(list(map(str, np.where(board[0:3, 6:9] == num)[0]))))
        box_val_count.append(len(list(map(str, np.where(board[3:6, 0:3] == num)[0]))))
        box_val_count.append(len(list(map(str, np.where(board[3:6, 3:6] == num)[0]))))
        box_val_count.append(len(list(map(str, np.where(board[3:6, 6:9] == num)[0]))))
        box_val_count.append(len(list(map(str, np.where(board[6:9, 0:3] == num)[0]))))
        box_val_count.append(len(list(map(str, np.where(board[6:9, 3:6] == num)[0]))))
        box_val_count.append(len(list(map(str, np.where(board[6:9, 6:9] == num)[0]))))

        for val in box_val_count:
            if val > 1:
                return True

    # If no duplicates, return false
    return False


def main():
    """Main program to solve sudoku from input file."""
    # Read file as input argument
    # TODO: Generalize input
    time_start = time.time()

    filename = sys.argv[1]
    print(str(filename))
    board = read_input(str(filename))

    # Print inital board
    print("Starting board:")
    print_board(board)
    print()

    # run solver
    naive_solver(board)
    time_end = time.time()

    # Print final board (solved or unsolved)
    print("Final board:")
    print_board(board)
    print("Solution took %.2f seconds" % (time_end - time_start))


if __name__ == "__main__":
    main()