# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False


# Will there be enough space?
def enough(cap, on, wait):
    if cap >= on + wait:
        return 0
    else:
        return wait - (cap - on)


# Are You Playing Banjo?
def areYouPlayingBanjo(name):
    if name.lower()[0] == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'


# Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'


# Counting sheep
def count_sheeps(sheep):
    number_of_sheep = 0
    for s in sheep:
        if s:
            number_of_sheep += 1
        else:
            number_of_sheep += 0
    return number_of_sheep


# Is this my tail?
def correct_tail(body, tail):
    length = len(body)
    sub = body[length - 1]
    if sub == tail:
        return True
    else:
        return False