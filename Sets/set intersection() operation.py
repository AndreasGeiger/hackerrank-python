amountNumbersFirst = int(input())
arrayFirst = set(map(int, input().split()))
amountNumbersSecond = int(input())
arraySecond = set(map(int, input().split()))

print(len(arrayFirst.intersection(arraySecond)))
