m = int(input())
arr1 = set([int(i) for i in (input()).split()])
n = int(input())
arr2 = set([int(i) for i in (input()).split()])

[print(i) for i in sorted(([i for i in arr1.difference(arr2)] + [i for i in arr2.difference(arr1)]))]
