from block import Block
from player import Player
from positions import Positioning
from positionManager import PositionManager
from random import randint
positionList = [Positioning.TOP, Positioning.BOTTOM, Positioning.RIGHT, Positioning.LEFT]

class Game:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.gameBoard = self.generateBoard()

        self.seeker = Player(0, 0, "seeker")
        self.setPlayerOnBoard(self.seeker.position.y, self.seeker.position.x, self.seeker)

        self.hider = Player(randint(1, column-1), randint(1, row-1), "hider")
        self.setPlayerOnBoard(self.hider.position.y, self.hider.position.x, self.hider)

        self.players = [self.seeker, self.hider]
        
 
    def setPlayerOnBoard(self, setRow, setCol, player):
        self.gameBoard[setRow][setCol].player = player

    def getBlock(self, blockRow, blockCol):
        return self.gameBoard[blockRow][blockCol]

    def movePlayer(self, player):
        while True:
            newPosition = positionList[randint(0,len(positionList)-1)]
            zombiePosition = PositionManager(player.position.x, player.position.y)
            newPlayerPosition = player.performAction(newPosition, self.row, self.column)

            if newPlayerPosition != False:
                print(newPosition)
                player.position = newPlayerPosition
                self.setPlayerOnBoard(zombiePosition.y, zombiePosition.x, None)
                self.setPlayerOnBoard(newPlayerPosition.y, newPlayerPosition.x, player)
                return
        
    def playerViewBlock(self, player):
        for x in positionList:
            viewPosition = player.performAction(positionList[i], self.row, self.column)

        if viewPosition != False:
            return self.getBlock(viewPosition.y, viewPosition.x).id
        return False

    def generateBoard(self):
        id = 0
        generatingBoard = []
        for ro in range (0, self.row):
            generatingBoard.append([])
            for col in range (0, self.column):
                block = Block(id)
                generatingBoard[ro].append(block) 
                id += 1 
        return generatingBoard 

    

game = Game(4,3)

for i in range(6):
    game.movePlayer(game.players[0])

print('x', game.players[0].position.x, 'y', game.players[0].position.y)


