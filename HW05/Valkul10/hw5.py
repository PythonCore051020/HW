#1
def zero_fuel(distance, mpg, fuel):
    if mpg*fuel>=distance:
	    print("You will make it")
	    return True
    else :
	    print("You won't make it")
	    return False
#2
def enough(cap, on, wait):
	if wait-(cap - on)<0 :
		return 0
	else :
		return wait-(cap-on)
print(enough(10, 10, 5))
#3
def areYouPlayingBanjo(name):
	if name.startswith("r") or name.startswith("R") :
		return name + " plays banjo"
	else :
		return name + " does not play banjo"
print(areYouPlayingBanjo("martin"))
#4
def bool_to_word(bool):
    if bool:
        return 'Yes'
    else:
        return 'No'
#5
def count_sheeps(sheep):
    count=0
    for s in sheep:
        if s==True:
            count=count+1
    return count
#6
def correct_tail(body, tail):
 return body.endswith(tail)





