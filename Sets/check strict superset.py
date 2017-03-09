setA =set(map(int,input().split()))
amountSets = int(input())

for i in range(amountSets):
    otherSet = set(map(int,input().split()))
    if(otherSet & setA == otherSet):
        answer ="True"
    else:
        answer ="False"
        break
print(answer)
