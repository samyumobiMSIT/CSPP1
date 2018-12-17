'''
Tictactoe.py
'''

def check_game(board, player):
    '''check the game'''
    game = False
    def check_rows(board, player):
        '''check the rows'''
        rows = False
        length = len(board)
        for i in range(length):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                rows = True
        return rows
    def check_cols(board, player):
        '''check colums'''
        cols = False
        for i in range(len(board)):
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                cols = True
        return cols
    def checkdiags(board, player):
        diags = False
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            diags = True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            diags = True
        return diags

    rows = check_rows(board, player)
    cols = check_cols(board, player)
    diag = checkdiags(board, player)
    if rows and cols:
        game = "Invalid"
    elif rows and diag:
        game = "Invalid"
    elif cols and diag:
        game = "Invalid"
    elif rows and cols and diag:
        game = "Invalid"
    elif rows or cols or diag:
        game = True
    return game

def main():
    '''Main Fucntion'''
    board = []
    ref = 'xo.'
    invalid_input = False
    for i in range(3):
        in_row = input().split()
        board.append(in_row)
        i += 1
        for j in in_row:
            if j not in ref:
                invalid_input = True

    x_game = check_game(board, 'x')
    o_game = check_game(board, 'o')
    if invalid_input:
        print("invalid input")
    elif x_game == "Invalid" or o_game == "Invalid":
        print("invalid game")
    elif x_game and o_game:
        print("invalid game")
    elif x_game:
        print("x")
    elif o_game:
        print("o")
    elif x_game is False and o_game is False:
        print("draw")

if __name__ == "__main__":
    main()
