#1
def count_positives_sum_negatives(arr):
    if arr == [] : return []
    pos_count = 0
    neg_count = 0
    for x in arr:
        if x > 0:
            pos_count += 1
        elif x < 0:
            neg_count+= x
    return [pos_count,neg_count]
##2
def reverse_list(l):
  l.reverse()
  return l
#3
def solution(number):
    result = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)
