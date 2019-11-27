from positions import Position, Positioning
from positionManager import PositionManager

class Player:
  view = Position.factory(Positioning.TOP)

  def __init__(self, xStart, yStart, id):
    self.position = PositionManager(xStart, yStart)
    self.id = id

  def performAction(self, newPosition, maxRow, maxColumn):
    tempPos = PositionManager(self.position.x, self.position.y)
    position = Position.factory(newPosition)
    tempPos = position.update(tempPos)

    if tempPos.validatePosition(maxRow, maxColumn):
      return tempPos
    else:
      return False


