class PositionManager:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def validatePosition(self, maxRow, maxColumn):
    if (self.x >= 0) and (self.y >= 0) and (self.x <= maxColumn-1) and (self.y <= maxRow-1):
      return True
    else:
      return False
