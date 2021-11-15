from collections import deque
def solution(progresses, speeds):
    answer = []
    size = len(progresses)
    index = 0

    while index < size:
        for i in range(index, size):
            progresses[i] = progresses[i] + speeds[i]

        count = 0
        temp = index
        for i in progresses[temp:]:
            if i >= 100:
                count += 1
                index += 1
            else:
                if count != 0:
                    answer.append(count)
                break
        if index == size:
            answer.append(count)

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))
print(solution([93, 30, 55], [1, 30, 5]))

# 조금더 깔끔하게 짜는 법을 생각해보자