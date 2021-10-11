import sys
import heapq

INF = int(1e9)
n, e = map(int, sys.stdin.readline().split())
distance = [[] for _ in range(n+1)]
start_dis = [INF] * (n+1)
v1_dis = [INF] * (n+1)
v2_dis = [INF] * (n+1)

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a].append((b, c))
    distance[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

def djstra(start, dis):
    q = []
    heapq.heappush(q, (0,start))
    dis[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > dis[now]:
            continue

        for i in distance[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


djstra(1, start_dis)
djstra(v1, v1_dis)
djstra(v2, v2_dis)

result = min(start_dis[v1] + v1_dis[v2] + v2_dis[n], start_dis[v2] + v2_dis[v1] + v1_dis[n])
if result >= INF:
    print(-1)
else:
    print(result)

# 복잡도를 계산할 경우도 다익스트라를 생각할 수 있게 되고, 문제 조건들 자체도 다익스트라를 선택하게 한다
# 다익스트라의 함수 자체를 이해하고 있다면 어렵지 않은 문제