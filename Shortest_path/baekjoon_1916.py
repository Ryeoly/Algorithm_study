import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    start, end, value = map(int, sys.stdin.readline().split())
    graph[start].append((end, value))

start, end = map(int, sys.stdin.readline().split())

def dijkstra(start):
    heap = list()
    heapq.heappush(heap, (0, start))
    while heap:
        value, cur = heapq.heappop(heap)

        if distance[cur] < value:
            continue
        for i in graph[cur]:
            cost = value + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijkstra(start)
print(distance[end])
