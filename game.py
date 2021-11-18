import numpy as np
import random
import outcomes

def flipcoin():
	if (np.random.uniform()>0.5):
		return "h"
	else:
		return "t"

def getscore(move, board):
	newboard = np.copy(board)
	newboard[move[0],move[1]] = comsymbol

	if (outcomes.win(newboard, comsymbol)):
		return 10


#board = np.full((3,3), '_')
board = np.array([['x','_','x'],
				  ['_','_','_'],
				  ['_','_','x']])

userguess = input("Heads or tails? (h/t): ")

if userguess==flipcoin():
	print("You can start the game. You are crosses")
	usersymbol = 'x'
	comsymbol = 'o'
else:
	print("I will start the game. You are noughts")
	usersymbol = 'o'
	comsymbol = 'x'



moves = np.argwhere(board=='_')

for i in range(len(moves)):
	getscore(moves[i,], board)


print(board)
