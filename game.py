from game2 import *
from getch import getch

class AlarmException(Exception):
	pass

def alarmHandler(signum, frame):
	raise AlarmException

def nonBlockingRawInput(prompt='', timeout=1):
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.alarm(timeout)
	try:
		print prompt,
		text = getch()
		signal.alarm(0)
		return text

	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''



class Gameplay(Block):

	def __init__(self):
		Block.__init__(self)


	def checkNextPosition(self, block, line, index):
		remIndex = index

		for i in block:
			for j in i:

				if (game[line][index] == 'X' or game[line][index] == '|' or game[line][index]== '-') and j == 'X':
					return False
				else:
					index += 1

			line += 1
			index = remIndex

		return True

	def checkRowFull(self):
		for i in range(1, 33):
			if game[30][i] == ' ':
				return False
		
		return True

	def ClearRow(self):

		if self.checkRowFull():

			for i in range(30, 0, -1):
				if i != 1:
					for j in range(1, 33):
						game[i][j] = game[i-1][j]

				else:
					for j in range(1, 33):
						game[1][j] = ' '
			
			self.updateScore(True)

			if self.checkRowFull():
				self.ClearRow()





def printbox(score):
	for i in game:
		for j in i:
			print j,
		print
	print '\n\n\n\n'        
	print "\t\t\tScore : ", score 




Tetris = Structure(30, 32);
brick = Gameplay()
2
Tetris.createbox()



while True:

	block, randomBlockno = brick.pickRandomBlock()
	pos = 0
	index = random.randrange(1, 30)

	gameover = 0

	if brick.checkGameover():
		gameover =1
		os.system('clear')
		print '\n\nGAMEOVER !!!'
		print 'Your Score is : ', brick.getScore()
		break

	if(brick.checkNextPosition(block, 1, index)):
		brick.assignPosition(block, 1, index)
		printbox(brick.getScore())


	itr=2
	blockStatus = 'target moved'

	while True:

		os.system('clear')

		if blockStatus == 'target moved' and itr <= 30:

			if brick.getScore() < 200:
				blockStatus = brick.move1Unit(index, block, itr)

			elif brick.getScore() < 500:
				blockStatus = brick.move1Unit(index, block, itr)
				if blockStatus == 'target moved':
					itr += 1
					blockStatus = brick.move1Unit(index, block, itr)

			else:
				blockStatus = brick.move1Unit(index, block, itr)
				if blockStatus == 'target moved':
					itr += 1
					blockStatus = brick.move1Unit(index, block, itr)

				if blockStatus == 'target moved':
					itr += 1
					blockStatus = brick.move1Unit(index, block, itr)



			if blockStatus == 'target blocked':
				break

			brick.ClearRow()
			printbox(brick.getScore())

			char = nonBlockingRawInput('\nEnter an Input : ')


			if char == 'd' and itr < 30:
				if brick.moveright(block, itr, index):
					index += 1
					
			elif char == 'a' and itr < 30:
				if brick.moveleft(block, itr, index):
					index -= 1

			elif char == 's' and itr < 30:
				rem_block = block
				rem_pos = pos

				brick.deassignPosition(index, block, itr)
				block, pos = brick.rotate(randomBlockno, pos)

				if not brick.checkNextPosition(block, itr+1, index):
					block = rem_block
					pos = rem_pos
					brick.assignPosition(block, itr, index)


			elif char == ' ' and itr < 30:
				while brick.move1Unit(index, block, itr+1) == 'target moved':
					itr += 1

				break


			itr+=1


		else:
			break

print '\n\n'
