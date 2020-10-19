# Return a string of the number
def number_to_string(num):
    num = str(num)
    return num
#Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
#Reversing Words in a String
def reverse(st):
    st = st.split()
    st = list(st)
    st2 = st[::-1]
    st2 = " ".join(st2)
    return st2