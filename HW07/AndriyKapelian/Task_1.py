# Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    pos_count = 0
    neg_sum = 0
    if arr:
        for num in arr:
            if num > 0:
                pos_count += 1
            elif num < 0:
                neg_sum += num
        answer = [pos_count, neg_sum]
        return answer
    else:
        return []


# Reverse List Order
def reverse_list(l):
    l.reverse()
    return l


# Multiples of 3 or 5
def solution(number):
    list_of_number = []
    r = 1
    sum_of_multiples = 0
    while r < number:
        list_of_number.append(r)
        r += 1
    for num in list_of_number:
        if num % 3 == 0 or num % 5 == 0:
            sum_of_multiples += num
    return sum_of_multiples