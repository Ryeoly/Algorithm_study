import heapq
def solution(n, edge):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    dis = [INF] * (n+1)
    dis[1] = 0

    for i in edge:
        graph[i[0]].append((i[1], 1))
        graph[i[1]].append((i[0], 1))

    q = []
    heapq.heappush(q, (0, 1))

    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    m_n = 0
    for i in range(2, n+1):
        if dis[i] != INF and dis[i] == m_n:
            answer += 1
        elif dis[i] != INF and dis[i] > m_n:
            answer = 1
            m_n = dis[i]

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))