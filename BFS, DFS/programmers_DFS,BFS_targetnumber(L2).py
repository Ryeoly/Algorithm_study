from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque([(numbers[0], 0), (-numbers[0], 0)])

    while que:
        value, pos = que.popleft()
        if value == target and pos == len(numbers)-1:
            answer += 1
        if pos + 1 < len(numbers):
            que.append((value + numbers[pos+1], pos+1))
            que.append((value - numbers[pos + 1], pos + 1))

    return answer