from block import Block
from player import Player
from viewSkill import View

class Board:
    @staticmethod
    def generateBoard(column, row):
        id = 0
        generatingBoard = []
        for col in range (0, column):
            generatingBoard.append([])
            for ro in range (0, row):
                block = Block(id)
                print(col)
                generatingBoard[col].append(block) 
                id += 1 
        return generatingBoard 

    def __init__(self, row, column):
        self.gameBoard = self.generateBoard(row, column)
        self.player1 = Player(0, 0, "player 1")
        self.setPlayerOnBoard(self.player1.position.x, self.player1.position.y, self.player1)
 

    def setPlayerOnBoard(self, column, row, player):
        self.gameBoard[row][column].occupied = player

    def getBlock(self, column, row):
        return self.gameBoard[column][row]

    def movePlayer(self, newPosition, player):
        zombiePlayer = Player(player.position.x, player.position.y, None)
        if(player.move(newPosition)):
            self.setPlayerOnBoard(zombiePlayer.position.y, zombiePlayer.position.x, None)
            self.setPlayerOnBoard(player.position.y, player.position.x, player)
        
    def playerViewBlock(self, player):
        tempPlayer =  Player(player.position.x, player.position.y, None)
        playerView = tempPlayer.getView().value.function(tempPlayer.position)
        return self.getBlock(playerView.y, playerView.x).id

    

board = Board(3,2)
print(board.movePlayer(View.RIGHT, board.player1))
print(board.playerViewBlock(board.player1))
print(board.player1.position.x, board.player1.position.y)
