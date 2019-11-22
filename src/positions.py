from enum import Enum

def topView(playerPosition):
  playerPosition.y -= 1
  return playerPosition

def bottomView(playerPosition):
  playerPosition.y += 1
  return playerPosition

def leftView(playerPosition):
  playerPosition.x -= 1
  return playerPosition


def rightView(playerPosition):
  playerPosition.x += 1
  return playerPosition


class Position:
  def __init__(self, label, function):
    self.label = label
    self.function = function

class Positions(Enum):
  TOP = Position("top", topView)
  BOTTOM = Position("bottom", bottomView)
  LEFT = Position("left", leftView)
  RIGHT = Position("right", rightView)


