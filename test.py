class Gameplay:

	def __init__(self, height, width):
		self.height = height;
		self.width = width;

	def createbox(self):

		game = [[0 for i in range(self.width+2)] for j in range(self.height+2)]
		for i in range(self.height+2):
			for j in range(self.width+2):

				if (i==0 and j==0) or (i==0 and j == self.width+1) or (i==self.height+1 and j==0) or (i == self.height+1 and j == self.width+1) :
					game[i][j] = '+'

				elif i == 0 and j >= 1 and j <= self.width:
					game[i][j] = '-'

				elif i == self.height+1 and j >=1 and j <= self.width:
					game[i][j] = '-'

				elif j == 0 and i >= 1 and i <= self.height:
					game[i][j] = '|'

				elif j == self.width+1 and i >= 1 and i <= self.height:
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

