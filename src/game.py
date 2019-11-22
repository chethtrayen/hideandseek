from block import Block
from player import Player, PlayerActions
from viewSkill import View

class Game:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.gameBoard = self.generateBoard()
        self.player1 = Player(0, 0, "player 1")
        self.setPlayerOnBoard(self.player1.position.x, self.player1.position.y, self.player1)
        
 
    def setPlayerOnBoard(self, newRow, newColumn, player):
        self.gameBoard[newRow][newColumn].player = player

    def getBlock(self, viewRow, viewCol):
        return self.gameBoard[viewRow][viewCol]

    def movePlayer(self, newPosition, player):
        tempPlayer = Player(player.position.x, player.position.y, None)
        if player.performAction(newPosition, self.row, self.column, PlayerActions.MOVE):
            self.setPlayerOnBoard(tempPlayer.position.y, tempPlayer.position.x, None)
            self.setPlayerOnBoard(player.position.y, player.position.x, player)
        
    def playerViewBlock(self, player):
        tempPlayer = Player(player.position.x, player.position.y, None)
        tempPlayer.view = player.view
        
        if player.performAction(tempPlayer.view, self.row, self.column, PlayerActions.MOVE):
            playerView = tempPlayer.view.value.function(tempPlayer.position)
            return self.getBlock(playerView.y, playerView.x).id

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

    

game = Game(4,2)

game.movePlayer(View.BOTTOM, game.player1)
game.movePlayer(View.RIGHT, game.player1)
game.movePlayer(View.BOTTOM, game.player1)
game.player1.view = View.LEFT
print('player1 view:', game.player1.view, game.playerViewBlock(game.player1))
print(game.player1.position.x, game.player1.position.y)
