from itertools import permutations
listA, listB = input().split()
listA.upper()
c=int(listB)
x=list(permutations(sorted(listA),c))
for i in x:
    print ("".join(i))
