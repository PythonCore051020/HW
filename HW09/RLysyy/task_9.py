import random


# task 9.1 https://www.codewars.com/kata/regular-ball-super-ball
class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# task 9.2 https://www.codewars.com/kata/color-ghost
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# task 9.3 https://www.codewars.com/kata/basic-subclasses-adam-and-eve
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


# task 9.4 https://www.codewars.com/kata/classy-classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"
