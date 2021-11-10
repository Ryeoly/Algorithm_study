n, m = map(int, input().split())

s = []
def dfs(start):
    for i in range(start, n+1):
        if len(s) == m:
            print(" ".join(map(str, s)))
            return
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)