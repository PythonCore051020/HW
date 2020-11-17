#1
class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type
#2
import random


class Ghost(object) :
	colors = ["white", "yellow", "purple", "red"]

	def __init__(self) :
		self.color = random.choice(Ghost.colors)
#3
def God():
    return [Man(), Woman()]

class Human: pass

class Man(Human): pass

class Woman(Human): pass
#4
class Person:
    def __init__(self,name,age):
        self.info=name+"s age is "+str(age)