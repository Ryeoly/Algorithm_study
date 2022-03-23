import sys


def find_parent(arr, number):
    if arr[number] == number:
        return number
    else:
        return find_parent(arr, arr[number])

def union_parent(arr, a, b):
    a = find_parent(arr, a)
    b = find_parent(arr, b)
    arr[max(a, b)] = min(a, b)

N, M = map(int, sys.stdin.readline().split())
INF = int(1e9)
arr = [i for i in range(N+1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    union_parent(arr, x, y)

for i in range(1, N+1):
    if arr[i] == i:
        continue
    else:
        arr[i] = find_parent(arr, i)

print(len(set(arr[1:])))