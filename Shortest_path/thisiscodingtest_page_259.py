import sys

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
distance = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            distance[i][j] = 0

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    distance[start][end] = 1
    distance[end][start] = 1

x, k = map(int, sys.stdin.readline().split())

for p in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][p]+distance[p][j])

result = distance[1][k]+distance[k][x]
if result >= INF:
    print(-1)
else:
    print(result)

# n, m의 범위가 100이하라는 조건이 있기 때문에 n^3으로 시간 제한에 걸리지 않으므로
# 구현이 쉬운 플로이드 워셜 알고리즘을 이용한다.