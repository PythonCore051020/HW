from functools import reduce


# task 8.1 https://www.codewars.com/kata/is-the-string-uppercase
def is_uppercase(inp):
    return inp.isupper()


# task 8.2 https://www.codewars.com/kata/sort-my-textbooks
def sorter(textbooks):
    return sorted(textbooks, key=str.lower)


# task 8.3 https://www.codewars.com/kata/remove-the-time
def shorten_to_date(long_date):
    return long_date.split(',')[0]

if __name__ == "__main__":
    print(f"is_uppercase: ", is_uppercase('DSFDEGF'))
    print(f"sorter: ", sorter(['Fff', 'AAS']))
    print(f"shorten_to_date: ", shorten_to_date('Monday February 2, 8pm'))
