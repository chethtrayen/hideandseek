from enum import Enum

def topView(positon):
  positon.y -= 1
  return positon

def bottomView(positon):
  positon.y += 1
  return positon

def leftView(positon):
  positon.x -= 1
  return positon


def rightView(positon):
  positon.x += 1
  return positon


class ViewManager:
  def __init__(self, label, function):
    self.label = label
    self.function = function

class View(Enum):
  TOP = ViewManager("top", topView)
  BOTTOM = ViewManager("bottom", bottomView)
  LEFT = ViewManager("left", leftView)
  RIGHT = ViewManager("right", rightView)


