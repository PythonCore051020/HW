import random
def make_move(sticks):
    sticks_check = sticks % 4
    return random.randint(1, 3) if sticks_check == 0 else sticks_check
