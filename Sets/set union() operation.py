amountNumbersFirst = int(input())
firstArray = set(map(int, input().split()))
amountNumbersSecond = int(input())
secondArray = set(map(int, input().split()))

print(len(firstArray.union(secondArray)))
