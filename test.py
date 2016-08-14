import random
import os
import time

game = [[0 for i in range(34)] for j in range(32)]

class Gameplay:

	def __init__(self, height, width):
		self.height = height;
		self.width = width;

	def createbox(self):

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

	

class Block:

	def __init__(self):
		self.block = [['X', 'X', 'X', 'X'], [['X', 'X'], ['X', 'X']], [['X', 'X'], [' ', 'X', 'X']], [[' ', 'X', 'X'], ['X', 'X']], [[' ', 'X'], ['X', 'X', 'X']], 
						[['X', 'X', 'X'], [' ', ' ', 'X']]]

	def pickRandomBlock(self):
		return self.block[random.randrange(0,6)] #return array of between index of 0 to 5


	def assignPosition(self, block, line, index):

		remIndex = index;

		#line=1
		if len(block) == 4: #1D - Array
			for i in block:
				game[line][index] = i;
				index +=1

		else: # 2-D Array
			for i in block:
				for j in i:
					game[line][index] = j
					index += 1
				line += 1
				index = remIndex

		return remIndex;

	def deassignPosition(self, remIndex, block, line):
		line=1
		remRemIndex = remIndex
		if len(block) == 4:
			for i in block:
				game[line][remIndex] = ' '
				remIndex += 1
		else:
			for i in block:
				for j in i:
					game[line][remIndex] = ' '
					remIndex += 1
				line += 1
				remIndex = remRemIndex



	def move1Unit(self, remIndex, block, line):
		
		# remRemIndex = remIndex

		# if len(block) == 4:
		# 	for i in block:
		# 		game[line][remIndex] = i
		# 		remIndex += 1
		# else:

		self.assignPosition(block, line, remIndex)




def printbox():
	for i in game:
		for j in i:
			print j,
		print


Tetris = Gameplay(30, 32);
brick = Block();

Tetris.createbox()
printbox()

print '\n\n\n'

time.sleep(1)
os.system('clear')

block = brick.pickRandomBlock()
remIndex = brick.assignPosition(block, 1, random.randrange(1, 30))
printbox()

print '\n\n\n'



brick.deassignPosition(remIndex, block, 1)
#printbox()

time.sleep(1)
os.system('clear')

brick.move1Unit(remIndex, block, 2)
printbox()

print '\n\n\n'



