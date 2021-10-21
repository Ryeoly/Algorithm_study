import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sets = set(arr)
_arr = list(sets)
_arr.sort()

dict = {}

for i in range(len(_arr)):
    dict[_arr[i]] = i

for i in range(n):
    print(dict[arr[i]], end=" ")