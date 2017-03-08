amountNumber = list(map(int, input().split()))
iNumbers = list(map(int,input().split()))
goodNumbers = set(map(int,input().split()))
badNumbers = set(map(int,input().split()))
happiness = 0

for i in range(len(iNumbers)):
    if iNumbers[i] in goodNumbers:
        happiness += 1

    if iNumbers[i] in badNumbers:
        happiness -= 1

print(happiness)
