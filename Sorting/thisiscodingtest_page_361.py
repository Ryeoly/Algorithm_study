def solution(N, stages):
    answer = dict()
    people = [0] * (N + 2)
    total = len(stages)

    for i in stages:
        people[i] += 1

    for i in range(1, N + 1):
        if total != 0:
            answer[i] = people[i] / total
            total -= people[i]
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x: answer[x], reverse = True)


print(solution(5, [2,1,2,6,2,4,3,3]))