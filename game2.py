import random
import os
import time
import signal

game = [[0 for i in range(34)] for j in range(32)]


class Structure:

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


class Board():

    def __init__(self, score):
        # self.blocks = [['X', 'X', 'X', 'X'], [['X', 'X'], ['X', 'X']], [['X', 'X'], [' ', 'X', 'X']], [[' ', 'X', 'X'], ['X', 'X']], [[' ', 'X'], ['X', 'X', 'X']], 
        #                 [['X', 'X', 'X'], [' ', ' ', 'X']]]
        self.status = None

        self.blocks =[

                        [ [['X', 'X', 'X', 'X']], [['X'], ['X'], ['X'], ['X']] ],

                        [ [['X', 'X'], ['X', 'X']] ],

                        [ [['X', 'X'], [' ', 'X', 'X']], [[ ' ', 'X' ], ['X', 'X'], ['X']] ],

                        [  [[' ', 'X', 'X'], ['X', 'X']], [['X'], ['X', 'X'], [' ', 'X']] ],

                        [ [[' ', 'X'], ['X', 'X', 'X']], [['X'], ['X', 'X'], ['X']], [['X', 'X', 'X'], [' ', 'X']], [[' ', 'X'], ['X', 'X'], [' ', 'X']] ],

                        [ [['X', 'X', 'X'], [' ', ' ', 'X']], [[' ', 'X'], [' ', 'X'], ['X', 'X']], [['X'], ['X', 'X', 'X']], [['X', 'X'], ['X'], ['X']] ],


                       ]

        self.score = score

    def pickRandomBlock(self):

        randomBlock = random.randrange(0,6)
        return self.blocks[randomBlock][0], randomBlock
        #return self.blocks[0][0], 0

    def open(self):
        self.status = True

    def rotate(self, randomBlockno, pos):

        mod = len(self.blocks[randomBlockno])
        block = self.blocks[randomBlockno][(pos+1)%mod]
        #self.deassignPosition(index, block, itr) 
        return block, (pos+1)%mod

    def assignPosition(self, block, line, index):

        remIndex = index;

        for i in block:
            for j in i:
                if game[line][index] != 'X' and j == 'X':
                    game[line][index] = j
                index += 1
            line += 1
            index = remIndex


    def deassignPosition(self, index, block, line):
        remIndex = index

        for i in block:
            for j in i:
                if j == 'X':
                    game[line][index] = ' '
                index += 1
            line += 1
            index = remIndex



    def move1Unit(self, index, block, line):

        self.deassignPosition(index, block, line-1)
        if(self.checkNextPosition(block, line, index)):
            self.assignPosition(block, line, index)
            return 'target moved'
        else:
            self.assignPosition(block, line-1, index)
            self.updateScore(False)
            return 'target blocked'

    def checkGameover(self):
        for i in range(1,33):
            if game[1][i] == 'X':
                return True

        return False



    def updateScore(self, rowClear):
        if rowClear == False:
            self.score += 10
        else:
            self.score += 100

    def getScore(self):
        return self.score


class Block(Board):

    def __init__(self):
        Board.__init__(self, 0)
        self.status = None

    def moveright(self, block, line, index):

        self.deassignPosition(index, block, line)
        if(self.checkNextPosition(block, line, index+1)):
            self.assignPosition(block, line, index+1)
            return True
        else:
            self.assignPosition(block, line, index)
            return False

    def open(self):
        self.status = False

    def moveleft(self, block, line, index):

        self.deassignPosition(index, block, line)
        if(self.checkNextPosition(block, line, index-1)):
            self.assignPosition(block, line, index-1)
            return True
        else:
            self.assignPosition(block, line, index)
            return False
