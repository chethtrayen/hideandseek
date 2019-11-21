class PositionManager:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def validatePosition(self):
    if self.x < 0 or self.y < 0 :
      return False
    else:
      return True
