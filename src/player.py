from viewSkill import View
from positionManager import PositionManager

class Player:

  view = View.TOP

  def __init__(self, xStart, yStart, label):
    self.position = PositionManager(xStart, yStart)
    self.id = id

  def setView(self, newView):
    self.view = newView

  def getView(self):
    return self.view

  def move(self, viewPosition):
    tempPos = PositionManager(self.position.x, self.position.y)
    tempPos = viewPosition.value.function(tempPos)
    if tempPos.validatePosition():
      self.position = tempPos
      return True
    else:
      return False
