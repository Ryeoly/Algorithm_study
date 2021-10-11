import sys

INF = int(1e9)
v, e = map(int, sys.stdin.readline().split())
distance = [[INF] * (v+1) for _ in range(v+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a][b] = c

for i in range(1, v+1):
    distance[i][i] = 0

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            distance[a][b] = min(distance[a][k]+distance[k][b], distance[a][b])

result = INF
for i in range(1, v+1):
    for j in range(1, v+1):
        if i != j:
            result = min(result, distance[i][j] + distance[j][i])

if result == INF:
    print(-1)
else:
    print(result)

# 시간 복잡도를 구해 2초 안에 돌아갈 줄 알았지만 이상하게 python3은 시간초과
# pypy3는 통과 되었다. 폴로이드 알고리즘으로 사이클을 구하는 방식
# 다음에는 다익스트라로 사이클을 구해보자.