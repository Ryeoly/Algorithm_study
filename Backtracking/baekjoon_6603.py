import sys

def dfs(start, dep):
    if dep == 6:
        print(" ".join(map(str,answer[0:6])))
        return

    for i in range(start, k):
        answer[dep] = arr[i]
        dfs(i+1, dep+1)


while 1:
    arr = list(map(int, sys.stdin.readline().split()))
    k = arr.pop(0)
    if k == 0:
        break

    answer = [0 for _ in range(13)]
    dfs(0, 0)
    print()
