import numpy as np
import random
import pandas
import time 
import outcomes


def display(board):
	print(pandas.DataFrame(board, columns=[1,2,3], index=[1,2,3]))

def flipcoin():
		if (random.randint(0,1)==1):
			return "h"
		else:
			return "t"


def make_a_move(board):

	def getscore(move, board):
		newboard = np.copy(board)
		newboard[move[0],move[1]] = comsymbol
		if (outcomes.win(newboard, comsymbol)):
			return (10,move)

		newboarduser = np.copy(board)
		newboarduser[move[0],move[1]] = usersymbol
		if (outcomes.block(newboarduser, usersymbol)):
			return (9,move)

		#add fork and block fork

		return (0,0);


	moves = np.argwhere(board=='_')
	bestmoves = []
	for i in range(len(moves)):
		bestmoves.append(getscore(moves[i,], board))

	bestmove = []
	bestmovescore = 0

	for move in bestmoves:
		if move[0]>bestmovescore:
			bestmovescore=move[0]
			bestmove = move[1]
	if len(bestmove)!=0:
		board[bestmove[0], bestmove[1]] = comsymbol
		return

	if (all(m==0) for m in bestmoves):
		if (board[1,1]=='_'):
			board[1,1]=comsymbol
			return
		elif((board[0,0]==usersymbol) & (str(board[2,2])=='_')):
			board[2,2]=comsymbol
			return
		elif((board[0,2]==usersymbol) & (str(board[2,0])=='_')):
			board[2,0]=comsymbol
			return 
		elif((board[2,0]==usersymbol) & (str(board[0,2])=='_')):
			board[0,2]=comsymbol
			return
		elif((board[2,2]==usersymbol) & (str(board[0,0])=='_')):
			board[0,0]=comsymbol
			return

	empty_corners=[]
	corners = [[0,0],[2,2],[0,2],[2,0]]
	for corner in corners:
		if board[corner[0],corner[1]]=='_':
			empty_corners.append(corner)
	index = random.choice(empty_corners)
	print(index)
	board[index[0],index[1]] = comsymbol
	return 

if __name__ == '__main__':
	done = False
	board = np.full((3,3), '_')

	userguess = input("Heads or tails? (h/t): ")

	if userguess==flipcoin():
		print("You can start the game. You are crosses")
		usersymbol, comsymbol = 'x', 'o'
	else:
		print("I will start the game. You are noughts")
		usersymbol, comsymbol = 'o', 'x'


	if usersymbol=='x':
		display(board)
		print("Make a move ")
		r = input("Row: ")
		c =input("Column: ")
	
		board[int(r),int(c)] = usersymbol
		display(board)

	while not done:
		print("Computer making move...")
		time.sleep(3)
		make_a_move(board)
		display(board)
		if outcomes.win(board, comsymbol):
			print("I think i have won")
			exit(0)
		print("Your turn... ")
		r = input("Row: ")
		c =input("Column: ")
	
		board[int(r),int(c)] = usersymbol
		display(board)

	






