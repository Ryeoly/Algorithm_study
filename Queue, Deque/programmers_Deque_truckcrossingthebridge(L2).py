from collections import deque
def solution(bridge_length, weight, truck_weights):
    sec = 0
    que = [0] * (bridge_length)
    que = deque(que)
    waits = deque(truck_weights)

    while waits:
        sec += 1
        que.pop()
        que.appendleft(0)

        if sum(que) + waits[0] <= weight:
            que[0] = waits.popleft()

    sec += bridge_length

    return sec
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
# while 조건을 1이 아닌 waits로 걸면서 실행시간을 줄였고
# 최대한 필요없는 조건문이나 문장을 줄임으로써 test5번을 해결했다.
