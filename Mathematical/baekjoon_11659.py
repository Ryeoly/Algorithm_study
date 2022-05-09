import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
value = [0] * 100002

for i in range(1, n+1):
    value[i] = value[i-1] + arr[i-1]

for q in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(value[j]-value[i-1])
