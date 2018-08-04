import sys
from random import *
import copy

from SudokuShared import *

class SudokuGame(object):

	def __init__(self,size):
		self.size = size
		self.board = self.create_board()
#The board will be like: 
#[
#[box,box,box],
#[box,box,box],
#[box,box,box]
#]
#and the boxes will be like:
#[
#[0,0,0]
#[0,0,0]
#[0,0,0]
#]
	
	def setup_board(self):
		self.board = self.create_board()
		self.solution = self.create_solution()
		self.create_final_board()

	def create_board(self):
		finalBoard = []
		for boxRow in range(self.size):
			rowToAdd = []
			for boxColumn in range(self.size):
				boxToAdd = []
				for row in range(self.size):
					toAdd = []
					for column in range(self.size):
						toAdd.append(0)
					boxToAdd.append(toAdd)
				rowToAdd.append(boxToAdd)
			finalBoard.append(rowToAdd)

		return finalBoard

	def create_solution(self):
		possibleMoves = []
		for boxRow in range(self.size):
			for boxColumn in range(self.size):
				possibleMoves.append([boxRow,boxColumn])

		done = False

		while not done:
			try:
				for num in range(1,(self.size**2)+1):
					for boardRow in range(self.size):
						for boardColumn in range(self.size):
							tempBoard = copy.deepcopy(self.board)
							currentPossibleMoves = possibleMoves[:]
							currentPick = choice(currentPossibleMoves)
							while check_move(tempBoard,boardRow,boardColumn,currentPick[0],currentPick[1],num) == False:
								tempBoard = copy.deepcopy(self.board)
								currentPossibleMoves.remove(currentPick)
								if len(currentPossibleMoves) <= 0:
									raise StopIteration
								currentPick = choice(currentPossibleMoves)
							tempBoard[boardRow][boardColumn][currentPick[0]][currentPick[1]] = num

							self.board = copy.deepcopy(tempBoard)
				done = True
			except StopIteration:
				self.board = self.create_board()
				pass

	def create_final_board(self):
		occupiedPositions = []
		for boxRow in range(self.size):
			for boxColumn in range(self.size):
				occupiedPositions.append([boxRow,boxColumn])

		for boardRow in range(self.size):
			for boardColumn in range(self.size):
				amountToTake = random.randint(1,self.size**2)
				currentOccupiedPositions = occupiedPositions[:]
				for x in range(amountToTake):
					currentPick = choice(currentOccupiedPositions)
					self.board[boardRow][boardColumn][currentPick[0]][currentPick[1]] = 0
					currentOccupiedPositions.remove(currentPick)

	def __str__(self):
		return board_to_string(self.board)

	def play(self,x,y,num):
		boardRow = y // self.size
		boardColumn = x // self.size
		boxRow = y - (boardRow*self.size)
		boxColumn = x - (boardColumn * self.size)

		if check_move(self.board,boardRow,boardColumn,boxRow,boxColumn,num) or num == 0:
			self.board[boardRow][boardColumn][boxRow][boxColumn] = num
			return True
		else:
			print("Cannot play there!")
			return False

			
testBoard1 =[
				[
					[
						[0,0],
						[0,1]
					],
					[
						[0,0],
						[0,0]
					]


				],
				[
					[
						[0,0],
						[0,0]
					],
					[
						[0,0],
						[0,0]
					]
				]
		 	]

if __name__=="__main__":
	boardSize = 0

	if len(sys.argv) == 2:
		boardSize = int(sys.argv[1])
	else:
		boardSize = 3

	game = SudokuGame(boardSize)
	game.create_solution()
	game.create_final_board()
	print(str(game))