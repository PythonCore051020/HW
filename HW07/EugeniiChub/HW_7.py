# Task_7.1
import math


def count_positives_sum_negatives(arr):
    ux = []
    c = 0
    s = 0
    for i in arr:
        if i > 0:
            c = c + 1
        else:
            s = s + i
    ux.append(c)
    ux.append(s)
    return ux


# Task_7.2
def reverse_list(l):
    l.reverse()
    return l


# Task_7.3
def solution(number):
    li = []
    lisum = 0
    for i in range(number):
        li.append(i)
    for i in range(number):
        if i % 3 == 0:
            li[i] = i
        elif i % 5 == 0:
            li[i] = i
        else:
            li[i] = 0
    print(li)
    for i in li:
        lisum = lisum + i
    return lisum
