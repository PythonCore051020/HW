#1
def is_uppercase(inp):
    return inp.isupper()
#2
def sorter(textbooks):
    return sorted(textbooks,key=str.lower)
#3
def shorten_to_date(long_date):
    splitc = long_date.find(',')
    return long_date[:splitc]
