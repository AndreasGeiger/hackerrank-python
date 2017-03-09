from itertools import product

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

productLists = list(product(listA, listB))

for i in range(len(productLists)):
    print(productLists[i], end=" ")

