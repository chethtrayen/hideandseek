from viewSkill import View
from positionManager import PositionManager
from enum import Enum

class Player:
  view = View.TOP

  def __init__(self, xStart, yStart, label):
    self.position = PositionManager(xStart, yStart)
    self.id = id

  def performAction(self, viewPosition, maxRow, maxColumn, action):
    tempPos = PositionManager(self.position.x, self.position.y)
    tempPos = viewPosition.value.function(tempPos)

    if tempPos.validatePosition(maxRow, maxColumn):
      if(PlayerActions.MOVE == action.MOVE):
        self.position = tempPos
      return True
    else:
      return False
  
class PlayerActions(Enum): 
  MOVE = 1
  VIEW = 1

