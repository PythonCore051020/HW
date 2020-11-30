# itr = [i for i in range(10)]
# gen = (i for i in range(10))
#
# print(itr)
# print(gen)
# print(next(gen))
# print(next(gen))

def myGen(s, e=10, step=1):
    i = s

    while i < e:
        yield i
        i += step
g = myGen(3)
print(g)
print(next(g))
