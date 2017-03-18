first, second = [int(x) for x in input().split()]
arrayN = []
for _i_ in range(first):
    arrayN.append([int(x) for x in input().split()][1:])

from itertools import product
possible_combination = list(product(*arrayN))

def func(nums):
    return sum(x*x for x in nums) % second

print(max(list(map(func, possible_combination))))
