from block import Block
from player import Player
from positions import Positions

class Game:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.gameBoard = self.generateBoard()
        self.seeker = Player(0, 0, "seeker")
        self.setPlayerOnBoard(self.seeker.position.x, self.seeker.position.y, self.seeker)
        self.players = [self.seeker]
        
 
    def setPlayerOnBoard(self, newRow, newColumn, player):
        self.gameBoard[newRow][newColumn].player = player

    def getBlock(self, viewRow, viewCol):
        return self.gameBoard[viewRow][viewCol]

    def movePlayer(self, newPosition, player):
        tempPlayer = Player(player.position.x, player.position.y, None)
        newPlayerPosition = player.performAction(newPosition, self.row, self.column, player.position)

        if newPlayerPosition != False:
            self.setPlayerOnBoard(tempPlayer.position.y, tempPlayer.position.x, None)
            self.setPlayerOnBoard(newPlayerPosition.y, newPlayerPosition.x, player)
        
    def playerViewBlock(self, player):
        viewPosition = player.performAction(player.view, self.row, self.column, player.position)
        if viewPosition != False:
            return self.getBlock(viewPosition.y, viewPosition.x).id

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

#game.movePlayer(Positions.BOTTOM, game.players[0])
game.movePlayer(Positions.RIGHT, game.players[0])
#game.movePlayer(Positions.RIGHT, game.players[0])
#game.movePlayer(Positions.BOTTOM, game.players[0])
#game.players[0].view = Positions.RIGHT
#print('players[0] view:', game.players[0].view, game.playerViewBlock(game.players[0]))
print(game.getBlock(0, 1).player)
print('x', game.players[0].position.x, 'y', game.players[0].position.y)


