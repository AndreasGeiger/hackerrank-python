groupSize = input()
groups = list(map(int,input().split(' ')))
tmpArray1 = set()
tmpArray2 = set()
for i in groups:
    if i in tmpArray1:
        tmpArray2.discard(i)
    else:
        tmpArray1.add(i)
        tmpArray2.add(i)

for i in tmpArray2:
    print(i)
