# Task_5.1
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / fuel_left <= mpg:
        return True
    else:
        return False


# Task_5.2
def enough(cap, on, wait):
    if cap - (on + wait) == 0:
        return 0
    else:
        return on - wait


# Task_5.3
def areYouPlayingBanjo(name):
    if name[0].upper() == "R":
        return print(name + " plays banjo")
    else:
        return print(name + " does not play banjo")


# Task_5.4
def bool_to_word(boolean):
    rez = ''
    if boolean == True:
        rez = 'Yes'
    else:
        rez = 'No'
    return rez


# Task_5.5
def count_sheeps(sheep):
    sheepcount = 0
    for i in sheep:
        if i == True:
            sheepcount += 1
    return sheepcount


# Task_5.6
def correct_tail(body, tail):
    if body[-1:] == tail:
        return True
    else:
        return False
