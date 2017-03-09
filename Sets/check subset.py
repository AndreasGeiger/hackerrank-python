testCases = int(input())

for i in range(testCases):
    numberElementsA = int(input())
    listA = list(map(int, input().split()))

    numberElementsB = int(input())
    listB = list(map(int, input().split()))

    for j in range(len(listA)):

        if listA[j] not in listB:
            print(False)
            break

        if j == len(listA) - 1:
            print(True)
