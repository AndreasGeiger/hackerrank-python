
amountNumbers = int(input())
listNumbers = map(int, input().split())
listNumbers = sorted(set(listNumbers))
print(listNumbers[-2])
