from collections import deque
import sys
import heapq

# bfs
def solution(n, k, x, arr):
    distance = [-1] * (n + 1)
    distance[x] = 0

    que = deque()
    que.append(x)

    while que:
        node = que.popleft()
        for connect_node in arr[node]:
            if distance[connect_node] == -1:
                distance[connect_node] = distance[node] + 1
                que.append(connect_node)

    evidence = -1
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
            evidence += 1

    if evidence == -1:
        print(-1)

n, m, k, x = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)

solution(n, k, x, arr)



# dijkstra
def solution(n, k, x, arr):
    distance = [int(1e9)]*(n+1)
    distance[x] = 0
    que = list()

    heapq.heappush(que,(0,x))

    while que:
        dis, now = heapq.heappop(que)
        if distance[now] < dis:
            continue
        for i in arr[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que,(cost,i[0]))

    evidence = False
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
            evidence = True

    if evidence == False:
        print(-1)


n, m, k, x = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append((b,1))

solution(n, k, x, arr)

