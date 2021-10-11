import sys

INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
distance = [[INF] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a][b] = min(distance[a][b], c)

for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n+1):
    for p in range(1, n+1):
        for q in range(1, n+1):
            distance[p][q] = min(distance[p][q], distance[p][k]+distance[k][q])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] >= INF:
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print(end="\n")

# 출력 조건 끝까지 읽어라!