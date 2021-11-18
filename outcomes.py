import numpy as np

def checkrow(b, comsymbol):
	for row in b:
		if (str(row[0])==comsymbol) & (str(row[1])==comsymbol) & (str(row[2])==comsymbol):
			return True
	return False

def win(board, comsymbol):
	if (checkrow(board, comsymbol)) | (checkrow(board.T, comsymbol)):
		return True
	elif (np.array_equal(np.diagonal(board), [comsymbol,comsymbol,comsymbol])):
		return True
	elif (np.array_equal(np.fliplr(board).diagonal(), [comsymbol,comsymbol,comsymbol])):
		return True
	else:
		return False