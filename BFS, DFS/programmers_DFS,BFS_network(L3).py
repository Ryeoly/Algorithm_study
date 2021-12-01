from collections import deque
def bfs(n, computers, que, visit):
    while que:
        pos = que.popleft()
        for i in range(0, n):
            if computers[pos][i] == 1 and visit[i] == 0:
                visit[i] = 1
                que.append(i)
    return visit

def solution(n, computers):
    answer = 0
    visit = [0] * n
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            visit = bfs(n, computers, deque([i]), visit)
            answer += 1

    return answer

# 문제는 몇개로 네트워크가 분리 되어있는가를 묻고 있다
# 1. 모든 node를 순차적으로 들러 연결된 Node들에 연결된 node들까지 저장하며
#    visit로 방문했다는 기록을 남겨, 나중에 중복될 경우를 배제
# 2. 1번에 연결된 모든 노드들이 visit에 기록되었으니 visit하지 않았던 다음
#    node를 찾아 연결된 node들을 다시 찾는다.
# 3. 1,2번 반복 후 새로운 네트워크로 들어갈 때마다 counting