import numpy as np

def checkrow(b, symbol):
	for row in b:
		if (str(row[0])==symbol) & (str(row[1])==symbol) & (str(row[2])==symbol):
			return True
	return False

def win(board, symbol):
	if (checkrow(board, symbol)) | (checkrow(board.T, symbol)):
		return True
	elif (np.array_equal(np.diagonal(board), [symbol,symbol,symbol])):
		return True
	elif (np.array_equal(np.fliplr(board).diagonal(), [symbol,symbol,symbol])):
		return True
	else:
		return False


def block(board, usersymbol):
	return win(board, usersymbol)
	