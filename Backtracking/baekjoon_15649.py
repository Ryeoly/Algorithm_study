import itertools

n, m = map(int, input().split())
arr = list()
for i in range(1, n+1):
    arr.append(str(i))
result = itertools.permutations(arr, m)

for i in result:
    print(" ".join(i))