# function that can transform a number into a string
def number_to_string(num):
    transformed_num = str(num)
    return transformed_num


# function that reverses the words in a given string
def reverse(st):
    # Your Code Here
    words = st.split()
    words = list(reversed(words))
    reversed_string = " ".join(words)
    return reversed_string


# fixing Jenny's function
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)