class Gameplay:

	def __init__(self, height, width):
		self.height = height;
		self.width = width;

	def createbox(self):

		game = [[0 for i in range(self.width)] for j in range(self.height)]
		for i in range(self.height):
			for j in range(self.width):
				if i == 0:
					game[i][j] = '-'

				elif i == self.height-1:
					game[i][j] = '-'

				elif j == 0:
					game[i][j] = '|'

				elif j == self.width-1:
					game[i][j] = '|'

				else:
					game[i][j] = ' '
		return game	

	def printbox(self, game):
		for i in game:
			for j in i:
				print j,
			print		



Tetris = Gameplay(30, 32);
game = Tetris.createbox()
Tetris.printbox(game)

