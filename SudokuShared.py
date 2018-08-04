import sys, random

def check_box(box, num):
	timesNumSeen = 0
	for row in range(len(box)):
		for column in range(len(box)):
			if box[row][column] == num:
				timesNumSeen += 1

	if timesNumSeen <= 1:
		return True
	return False
	
def check_horizontal(board, num):
	for boardRow in range(len(board)):
		for boxRow in range(len(board)):
			timesNumSeen = 0
			for boardColumn in range(len(board)):
				for boxColumn in range(len(board)):
					if board[boardRow][boardColumn][boxRow][boxColumn] == num:
						timesNumSeen += 1
					#print(str(timesNumSeen) + " ",end="")
			#print("")
			if timesNumSeen > 1:
				return False
	return True


def check_vertical(board,num):
	for boardColumn in range(len(board)):
		for boxColumn in range(len(board)):
			timesNumSeen = 0
			for boardRow in range(len(board)):
				for boxRow in range(len(board)):
					if board[boardRow][boardColumn][boxRow][boxColumn] == num:
						timesNumSeen += 1
			if timesNumSeen > 1:
				return False
	return True

def check_number_placements(board, num):
	for boxRow in range(len(board)):
		for boxColumn in range(len(board)):
			if check_box(board[boxRow][boxColumn], num) == False:
				return False
	#print("Checked boxes")

	#if not check_horizontal(board, num):
	#	return False
	#print("Checked horizontal")

	#if not check_vertical(board,num):
	#	return False
	#print("Checked vertical")

	return check_horizontal(board, num) and check_vertical(board, num)

def check_move(board, boardRow, boardCol, boxRow, boxCol, num):
	newBoard = board.copy()

	if newBoard[boardRow][boardCol][boxRow][boxCol] == 0:
		newBoard[boardRow][boardCol][boxRow][boxCol] = num
	else:
		return False
	#print(boxRow, boxCol)
	#print("New board:")
	#print_board(newBoard)
	return check_number_placements(newBoard, num)

def board_to_string(board):
	finalString = ""
	for boardRow in range(len(board)):
		for boxRow in range(len(board)):
			stringToPrint = ""
			for boardColumn in range(len(board)):
				for boxColumn in range(len(board)):
					stringToPrint += str(board[boardRow][boardColumn][boxRow][boxColumn])
					stringToPrint += " "
				stringToPrint += " "
			finalString += stringToPrint
			finalString += "\n"
		finalString += "\n"

	return finalString

def print_board(board):
	print(board_to_string(board))