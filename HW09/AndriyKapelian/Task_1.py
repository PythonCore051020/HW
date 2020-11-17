# Regular Ball Super Ball
class Ball(object):

    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# Color Ghost
import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# Basic subclasses - Adam and Eve
def God():
    return [Man(), Woman()]

class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass


# Classy Classes
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = "{}s age is {}".format(name, age)
