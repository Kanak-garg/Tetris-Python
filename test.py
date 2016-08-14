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
		self.block = ['X', 'X', 'X', 'X']
		

	def assignPosition(self):

		index = random.randrange(1, 30) #random number between 1 to 29
		remIndex = index;
		if ''.join(self.block) == 'XXXX':
			for i in self.block:
				game[1][index] = i;
				index +=1
		return remIndex;

	def deassignPosition(self, remIndex):
		if ''.join(self.block) == 'XXXX':
			for i in self.block:
				game[1][remIndex] = ' '
				remIndex += 1


	def move1Unit(self, remIndex):
		if ''.join(self.block) == 'XXXX':
			for i in self.block:
				game[2][remIndex] = i
				remIndex += 1




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

remIndex = brick.assignPosition()
printbox()

print '\n\n\n'



brick.deassignPosition(remIndex)


time.sleep(1)
os.system('clear')

brick.move1Unit(remIndex)
printbox()

print '\n\n\n'



