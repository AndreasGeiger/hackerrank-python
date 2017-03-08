numberElementsA = int(input())
setA = set(map(int, input().split()))
numberOtherSets = int(input())

for i in range(numberOtherSets):
    command = input().split()
    otherSet = set(map(int, input().split()))

    if command[0] == "intersectioin_update":
        setA.intersection_update(otherSet)
    elif command[0] == "update":
        setA.update(otherSet)
    elif command[0] == "symmetric_difference_update":
        setA.symmetric_difference_update(otherSet)
    elif command[0] == "difference_update":
        setA.difference_update(otherSet)

print(sum(setA))
