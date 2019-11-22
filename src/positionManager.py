class PositionManager:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  @staticmethod
  def validatePosition(position, maxRow, maxColumn):
    if (position.x >= 0) and (position.y >= 0) and (position.x <= maxColumn-1) and (position.y <= maxRow-1):
      return True
    else:
      return False
