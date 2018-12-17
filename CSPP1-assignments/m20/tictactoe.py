def displayboard(board):
	for i in board:
		for j in i:
			print(j ," " ,end='')
		print()
def insertX(player1,board):	
	for i in range(len(board)):
		for j in range(len(board)):
			if i == player1[0] and j == player1[1] and board[i][j] == '_':
				board[i][j] = 'X'
	return board
def insertO(player2,board):
	for i in range(len(board)):
		for j in range(len(board)):
			if i == player2[0] and j == player2[1] and board[i][j] == '_':
				board[i][j] = 'O'
	return board
def checkGame(board, player):
	game = False
	def checkRows(board, player):
		rows = False
		for i in range(len(board)):
			if board[i][0] == player and board[i][1] == player and board[i][2] == player:
				rows = True
		return rows
	def checkCols(board, player):
		cols = False
		for i in range(len(board)):
			if board[0][i] == player and board[1][i] == player and board[2][i]== player:
				cols = True
		return cols
	def checkdiags(board, player):
		diags = False
		if board[0][0] == player and board[1][1] == player and board[2][2] == player:
			diags = True
		if board[0][0] == player and board[1][1] == player and board[2][2] == player:
			diags = True 
		return diags


	rows = checkRows(board, player)
	cols = checkCols(board, player)
	diag = checkdiags(board, player)
	if rows == True or cols == True or diag == True:
		game = True
	return game
 

def main():
	board = [['_','_','_'], ['_','_','_'], ['_','_','_']]
	displayboard(board)
	while True:
		player1 = input("Player 1 turn: ")
		player1 = player1.split()
		player1 = list(map(int, player1))
		board  = insertX(player1, board)
		displayboard(board)		
		play1 = checkGame(board, 'X')
		if play1 == True:
			print("player 1 wins")
			break
		player2 = input("Player 2 turn: ")
		player2 = player2.split()
		player2 = list(map(int, player2))
		board  = insertO(player2, board)
		displayboard(board)
		play2 = checkGame(board, '0')
		if play2 == True:
			print("player 2 wins")
			break
		



if __name__ == "__main__":
	main()
