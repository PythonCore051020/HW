#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    is_fuel = False
    if mpg * fuel_left >= distance_to_pump:
        is_fuel = True    
    return is_fuel

        