# import sys
#
# N, M, K, X = map(int, sys.stdin.readline().split())
# arr = [[0]*(N+1) for _ in range(N+1)]
# distance = [0] * (N+1)
# for i in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     arr[a][b] = 1
#
# for i in range(M+1):
#     temp = arr[X].copy()
#     for p in range(N+1):
#         if arr[X][p] > 0:
#             for q in range(N+1):
#                 if arr[X][q] == 0 and arr[p][q] > 0:
#                     arr[X][q] = arr[X][p]+arr[p][q]
#
#     if temp == arr[X]:
#         break
#
# result = list()
# for i in range(N+1):
#     if arr[X][i] == K:
#         result.append(i)
# if len(result) == 0:
#     print(-1)
# else:
#     for i in result:
#         print(i)
#

# bfs
from collections import deque


def solution(n, m, k, x, arr):
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

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

solution(n, m, k, x, arr)