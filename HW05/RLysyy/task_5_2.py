#Will there be enough space?
def enough(cap, on, wait):
    # Your code here
    retult = 0
    free_seats = cap - on 
    if free_seats < wait:
        retult = wait - free_seats
    return retult
       