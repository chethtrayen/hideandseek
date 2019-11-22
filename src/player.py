from positions import Positions
from positionManager import PositionManager
from enum import Enum

class Player:
  view = Positions.TOP

  def __init__(self, xStart, yStart, label):
    self.position = PositionManager(xStart, yStart)
    self.id = id

  @staticmethod
  def performAction(newPosition, maxRow, maxColumn, playerPosition):
    tempPos = newPosition.value.function(playerPosition)
  
    if tempPos.validatePosition(tempPos, maxRow, maxColumn):
      return tempPos
    else:
      return False

