from collections import deque
def solution(priorities, location):
    answer = 1
    que = deque()
    for i in range(len(priorities)):
        que.append((priorities[i],i))

    while que:
        if que[0][0] == max(que)[0]:
            if que[0][1] == location:
                return answer
            else:
                que.popleft()
                answer += 1
        else:
            que.rotate(-1)
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

# 쉽게 해결할 수 있었다. 다른 사람 코드와 비교해보는 습관을 들이자
# 효율적인 코드는 흡수하자