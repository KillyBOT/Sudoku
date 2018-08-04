import sys
from SudokuGame import *
from SudokuShared import *
import pygame

class SudokuGUI(object):

	def __init__(self, size):

		pygame.init()
		pygame.font.init()

		self.game = SudokuGame(size)

		self.running = False

		self.fillColor = (255,255,255)

		self.boxColor = (200,200,200)
		self.squareColor = (100,100,100)
		self.selectedColor = (0,128,0)
		self.hoverColor = (0,0,128)

		self.padding = 2
		self.squareSize = 40
		self.boxSize = ((self.squareSize)*self.game.size)+self.padding*(self.game.size+1)

		self.width = self.boxSize*self.game.size + 200
		self.height = self.boxSize*self.game.size + 50

		self.font = pygame.font.Font("Fonts/superstar.ttf", self.squareSize)
		self.textFont = pygame.font.Font("Fonts/superstar.ttf", 16)

		self.mouseX = 0
		self.mouseY = 0

		self.hoverX = 0
		self.hoverY = 0

		self.selectedX = 0
		self.selectedY = 0

		self.createNewBoardRect = pygame.Rect(self.boxSize*self.game.size+self.padding*4,self.padding,124,self.squareSize+self.padding*2)
		self.newBoardText = self.textFont.render("Create New Board", True, (0,0,0))

		self.loadingText = self.font.render("Loading...", True, (0,0,0))

		self.clock = pygame.time.Clock()

	def drawBoard(self):
		for x in range(self.game.size):
			for y in range(self.game.size):
				pygame.draw.rect(self.display, self.boxColor, pygame.Rect(x*self.boxSize,y*self.boxSize,self.boxSize,self.boxSize))
				for boxX in range(self.game.size):
					for boxY in range(self.game.size):
						renderColor = self.squareColor
						if (x * self.game.size) + boxX == self.hoverX and (y * self.game.size) + boxY == self.hoverY:
							renderColor = self.hoverColor
						elif (x * self.game.size) + boxX == self.selectedX and (y * self.game.size) + boxY == self.selectedY:
							renderColor = self.selectedColor

						pygame.draw.rect(self.display, renderColor, pygame.Rect((x*self.boxSize) + (boxX*self.squareSize) + self.padding*(boxX+1), (y*self.boxSize) + (boxY*self.squareSize) + self.padding*(boxY+1), self.squareSize, self.squareSize))

						text = self.font.render(str(self.game.board[x][y][boxX][boxY]), True, (0,0,0))
						self.display.blit(text, ((x*self.boxSize) + (boxX*self.squareSize) + self.padding*(boxX+3), (y*self.boxSize) + (boxY*self.squareSize)+self.padding*(boxY+3), self.squareSize, self.squareSize))

	def render(self):
		self.display.fill(self.fillColor)

		pygame.draw.rect(self.display, self.boxColor, self.createNewBoardRect)
		self.display.blit(self.newBoardText, (self.createNewBoardRect.x + self.padding, self.createNewBoardRect.y + self.createNewBoardRect.height//2))

		self.drawBoard()

		pygame.display.flip()

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.MOUSEMOTION:
				position = event.pos
				self.mouseX = position[0]
				self.mouseY = position[1]

				if self.mouseX < self.boxSize*self.game.size or self.mouseY < self.boxSize*self.game.size:
					self.hoverX = self.mouseX // (self.squareSize+self.padding)
					self.hoverY = self.mouseY // (self.squareSize+self.padding)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if self.mouseX < self.boxSize*self.game.size or self.mouseY < self.boxSize*self.game.size:
						self.selectedX = self.mouseX // (self.squareSize+self.padding)
						self.selectedY = self.mouseY // (self.squareSize+self.padding)

					if self.mouseX > self.createNewBoardRect.x and self.mouseY > self.createNewBoardRect.y and self.mouseX < self.createNewBoardRect.x + self.createNewBoardRect.width and self.mouseY < self.createNewBoardRect.y + self.createNewBoardRect.height:
						print("Loading new game...")
						self.game.setup_board()
						print("Done!")

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: self.running = False
				if event.key == pygame.K_w and self.selectedY > 0: 
					self.selectedY -= 1
				if event.key == pygame.K_s and self.selectedY < (self.game.size**2)-1: 
					self.selectedY += 1
				if event.key == pygame.K_a and self.selectedX > 0: 
					self.selectedX -= 1
				if event.key == pygame.K_d and self.selectedX < (self.game.size**2)-1: 
					self.selectedX += 1

				if event.key == pygame.K_0:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 0)
				if event.key == pygame.K_1:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 1)
				if event.key == pygame.K_2:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 2)
				if event.key == pygame.K_3:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 3)
				if event.key == pygame.K_4:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 4)
				if event.key == pygame.K_5:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 5)
				if event.key == pygame.K_6:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 6)
				if event.key == pygame.K_7:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 7)
				if event.key == pygame.K_8:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 8)
				if event.key == pygame.K_9:
					self.game.play(self.selectedY, self.selectedX, 0)
					self.game.play(self.selectedY, self.selectedX, 9)

			if self.game.board == self.game.solution:
				print("You win!")
				self.running = False

	def run(self):

		self.running = True

		#self.game.setup_board()

		self.display = pygame.display.set_mode((self.width,self.height))

		while self.running:
			self.handle_events()
			self.render()
		self.clock.tick(60)

		pygame.quit()

if __name__ == "__main__":

	boardSize = 0

	if len(sys.argv) == 2:
		boardSize = int(sys.argv[1])
	else:
		boardSize = 3

	game = SudokuGUI(boardSize)
	game.run()
	#print(str(game))


