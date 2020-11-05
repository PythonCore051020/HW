# Task_6.1
def distance(x1, y1, x2, y2):
    dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dist


# Task_6.2

# Task_6.3
def filter_words(st):
    st = st.lower()
    st = st.capitalize()
    return st


# Task_6.4
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i = i + 1
    return res
