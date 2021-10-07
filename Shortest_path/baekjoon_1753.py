import sys
import heapq

INF = int(1e9)
v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

distance = [INF] * (v+1)
road = [[] for _ in range(v+1)]

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    road[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in road[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in distance[1:]:
    if i < INF:
        print(i)
    else:
        print("INF")