# Is the string uppercase?
def is_uppercase(inp):
    if inp.isupper():
        return True
    else:
        return False


# Sort My Textbooks
def sorter(textbooks):
    textbooks.sort(key=str.lower)
    return textbooks


# Remove the time
def shorten_to_date(long_date):
    date_to_list = long_date.split(',')
    date_to_list.pop()
    return ",".join(date_to_list)


