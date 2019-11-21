from fovPositions import FovPosition

class PositionManager:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Player:
  fovPos = FovPosition.TOP

  def __init__(self, xStart, yStart):
    self.position = PositionManager(xStart, yStart)

  def setFovPos(self, newPos):
    self.fovPos = newPos

  def getBlockDetails(self):
    tempPos = PositionManager(self.position.x, self.position.y)
    tempPos = self.fovPos(tempPos)
    print(tempPos.y)       
    

player1 = Player(1,1)

print(player1.getBlockDetails())