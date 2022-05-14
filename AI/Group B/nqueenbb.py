def isSafe(board,r,c,N):
    # check row n col
    for  k in range(N):
        if board[r][k]==1 or board[k][c]==1:
            return False
    # check diagonal
    i,j=r,c
    while(i>=0 and j>=0) :  # left upper diagonal
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i,j=r,c
    while (j>=0 and i<N):  # right upper diagonal 
        if board[i][j]==1:
            return False
        j-=1
        i+=1

    return True
    """ Python3 program to solve N Queen Problem
using Branch or Bound """

N = 4

""" A utility function to print solution """
def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()

""" A Optimized function to check if
a queen can be placed on board[row][col] """
def isSafe(r, c, 
		rowLookup, slashCodeLookup,
					backslashCodeLookup):
	if (slashCodeLookup[r+c] or
		backslashCodeLookup[(r-c+N-1)] or
		rowLookup[r]):
		return False
	return True

""" A recursive utility function
to solve N Queen problem """
def solveNQueensUtil(board, col, 
					rowLookup, slashCodeLookup,
					backslashCodeLookup):
						
	""" base case: If all queens are
	placed then return True """
	if(col >= N):
		return True
	for i in range(N):
		if(isSafe(i, col,
				rowLookup, slashCodeLookup,
				backslashCodeLookup)):
					
			""" Place this queen in board[i][col] """
			board[i][col] = 1
			rowLookup[i] = True
			slashCodeLookup[i+col] = True
			backslashCodeLookup[i-col+N-1] = True
			
			""" recur to place rest of the queens """
			if(solveNQueensUtil(board, col + 1,
								
								rowLookup, slashCodeLookup,
								backslashCodeLookup)):
				return True
			
			""" If placing queen in board[i][col]
			doesn't lead to a solution,then backtrack """
			
			""" Remove queen from board[i][col] """
			board[i][col] = 0
			rowLookup[i] = False
			slashCodeLookup[i+col] = False
			backslashCodeLookup[i-col+N-1] = False
			
	""" If queen can not be place in any row in
	this column col then return False """
	return False

""" This function solves the N Queen problem using
Branch or Bound. It mainly uses solveNQueensUtil()to
solve the problem. It returns False if queens
cannot be placed,otherwise return True or
prints placement of queens in the form of 1s.
Please note that there may be more than one
solutions,this function prints one of the
feasible solutions."""
def solveNQueens():
	board = [[0 for i in range(N)]
				for j in range(N)]
	
	# helper matrices
	slashCode = [[0 for i in range(N)]
					for j in range(N)]
	backslashCode = [[0 for i in range(N)]
						for j in range(N)]
	
	# arrays to tell us which rows are occupied
	rowLookup = [False] * N
	
	# keep two arrays to tell us
	# which diagonals are occupied
	x = 2 * N - 1
	slashCodeLookup = [False] * x
	backslashCodeLookup = [False] * x
	
# 	# initialize helper matrices
# 	for rr in range(N):
# 		for cc in range(N):
# 			slashCode[rr][cc] = rr + cc
# 			backslashCode[rr][cc] = rr - cc + 7
	
	if(solveNQueensUtil(board, 0,
						rowLookup, slashCodeLookup,
						backslashCodeLookup) == False):
		print("Solution does not exist")
		return False
		
	# solution found
	printSolution(board)
	return True

# Driver Cde
solveNQueens()