from enum import Enum

class Positioning(Enum):
  TOP = 'top'
  BOTTOM = 'bottom'
  RIGHT = 'right'
  LEFT = 'left'


class Top():
  label = Positioning.TOP
  @staticmethod
  def update(position):
      position.y -= 1
      return position

class Bottom():
  label = Positioning.BOTTOM
  @staticmethod
  def update(position):
      position.y += 1
      return position

class Right():
  label = Positioning.RIGHT
  @staticmethod
  def update(position):
      position.x += 1
      return position

class Left():
  label = Positioning.LEFT
  @staticmethod
  def update(position):
      position.x -= 1
      return position

class Position:
  @staticmethod
  def factory(position):
    if position == Positioning.TOP:
      return Top()
    if position == Positioning.BOTTOM:
      return Bottom()
    if position == Positioning.RIGHT:
      return Right()
    if position == Positioning.LEFT:
      return Left()
    else:
      return Top()



