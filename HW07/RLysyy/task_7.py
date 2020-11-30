from functools import reduce


# task 7.1 https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    return [
        reduce((lambda x, y: x + 1), filter(lambda x: x > 0, arr), 0),
        reduce((lambda x, y: x + y), filter(lambda x: x < 0, arr), 0)
    ]


# task 7.2 https://www.codewars.com/kata/reverse-list-order
def reverse_list(l):
    return l[::-1]


# task 7.3 https://www.codewars.com/kata/multiples-of-3-or-5
def solution(number):
    return reduce(
        lambda x, y: x + y,
        filter(
            lambda x: x % 3 == 0 or x % 5 == 0,
            list(range(1, number))
        ), 0)


if __name__ == "__main__":
    print(f"count_positives_sum_negatives: ", count_positives_sum_negatives([]))
    print(f"reverse_list: ", reverse_list([1, 2]))
    print(f"solution: ", solution(10))
