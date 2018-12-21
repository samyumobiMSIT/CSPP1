def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if "".join(sorted(
            sudoku[0][0] + sudoku[0][1] + sudoku[0][2] + sudoku[1][0] + sudoku[1][1] + sudoku[1][2] + sudoku[2][0] +
            sudoku[2][1] + sudoku[2][2])) != "123456789":
        return False
    if "".join(sorted(
            sudoku[0][3] + sudoku[0][4] + sudoku[0][5] + sudoku[1][3] + sudoku[1][4] + sudoku[1][5] + sudoku[2][3] +
            sudoku[2][4] + sudoku[2][5])) != "123456789":
        return False
    if "".join(sorted(
            sudoku[0][6] + sudoku[0][7] + sudoku[0][8] + sudoku[1][6] + sudoku[1][7] + sudoku[1][8] + sudoku[2][6] +
            sudoku[2][7] + sudoku[2][8])) != "123456789":
        return False
    if "".join(sorted(
            sudoku[3][0] + sudoku[3][1] + sudoku[3][2] + sudoku[4][0] + sudoku[4][1] + sudoku[4][2] + sudoku[5][0] +
            sudoku[5][1] + sudoku[5][2])) != "123456789":
        return False
    if "".join(sorted(
            sudoku[3][3] + sudoku[3][4] + sudoku[3][5] + sudoku[4][3] + sudoku[4][4] + sudoku[4][5] + sudoku[5][3] +
            sudoku[5][4] + sudoku[5][5])) != "123456789":
        return False
    if "".join(sorted(
            sudoku[3][6] + sudoku[3][7] + sudoku[3][8] + sudoku[4][6] + sudoku[4][7] + sudoku[4][8] + sudoku[5][6] +
            sudoku[5][7] + sudoku[5][8])) != "123456789":
        return False
    if "".join(sorted(
            sudoku[6][0] + sudoku[6][1] + sudoku[6][2] + sudoku[7][0] + sudoku[7][1] + sudoku[7][2] + sudoku[8][0] +
            sudoku[8][1] + sudoku[8][2])) != "123456789":
        return False
    if "".join(sorted(
            sudoku[6][3] + sudoku[6][4] + sudoku[6][5] + sudoku[7][3] + sudoku[7][4] + sudoku[7][5] + sudoku[8][3] +
            sudoku[8][4] + sudoku[8][5])) != "123456789":
        return False
    if "".join(sorted(
            sudoku[6][6] + sudoku[6][7] + sudoku[6][8] + sudoku[7][6] + sudoku[7][7] + sudoku[7][8] + sudoku[8][6] +
            sudoku[8][7] + sudoku[8][8])) != "123456789":
        return False
    return True


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))


if __name__ == '__main__':
    main()