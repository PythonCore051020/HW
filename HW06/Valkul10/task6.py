#1
import math
def distance(x1, y1, x2, y2):
   distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
   return round(distance,2)

print(distance(1, 1, 0, 0))
#3
def filter_words(st):
    a = st.lower()
    b = a.capitalize()
    c = ' '.join(b.split())
    return c
#4
print(filter_words('HELLO world!'))
def create_array(n):
    res=[]
    i=1
    while i<=n:
	    res+=[i]
	    i = i + 1
    return res
print((create_array(1)))
#2
def make_move(sticks):
    while sticks < 21:
        return sticks%4
    else:
        return 1