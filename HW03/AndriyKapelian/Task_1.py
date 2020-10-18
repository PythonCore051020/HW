zen_of_python = '''The Zen of Python, by Tim Peters
   ....: Beautiful is better than ugly.
   ....: Explicit is better than implicit.
   ....: Simple is better than complex.
   ....: Complex is better than complicated.
   ....: Flat is better than nested.
   ....: Sparse is better than dense.
   ....: Readability counts.
   ....: Special cases aren't special enough to break the rules.
   ....: Although practicality beats purity.
   ....: Errors should never pass silently.
   ....: Unless explicitly silenced.
   ....: In the face of ambiguity, refuse the temptation to guess.
   ....: There should be one-- and preferably only one --obvious way to do it.
   ....: Although that way may not be obvious at first unless you're Dutch.
   ....: Now is better than never.
   ....: Although never is often better than *right* now.
   ....: If the implementation is hard to explain, it's a bad idea.
   ....: If the implementation is easy to explain, it may be a good idea.
   ....: Namespaces are one honking great idea -- let's do more of those!'''

# count of words
list_of_words = ['better', 'never', 'is']

for word in list_of_words:
    count = zen_of_python.lower().count(word)
    print('Words %s appears %d times' % (word, count))
print('\n')

# print zen in upper case
zen_of_python_upper_case = zen_of_python.upper()
print(zen_of_python_upper_case + '\n')

# replace i to &
zen_of_python_without_i = zen_of_python.lower().replace('i', '&')
print(zen_of_python_without_i + '\n')

