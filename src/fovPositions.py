from enum import Enum

def topViewFunction(self, positon):
  positon.y -= 1
  return positon


class FovPosition(Enum):
  TOP = topViewFunction
  BOTTOM = 1
  LEFT = 2
  RIGHT = 3


