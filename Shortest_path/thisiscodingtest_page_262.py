import sys
import heapq

INF = int(1e9)
n, m, c = map(int, sys.stdin.readline().split())

road = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    road[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in road[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)
count = 0
time = 0
for i in distance:
    if i != INF:
        count += 1
        time = max(time, i)
print(count-1, time)

# 기준인 한 도시에서 각 도시들간의 거리를 구하라 함으로 다익스트라를 떠올릴 수 있다.
# 위의 기준이 아니더라고 n의 범위로 인해 다익스트라로 구현해야 한다는 감이 온다.