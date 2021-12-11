import heapq

def solution(jobs):
    answer = 0
    waits = list()
    time = 0
    pos = 0
    jobs.sort(key= lambda x : x[0])

    while pos < len(jobs) or waits:
        # jobs에서 들어올 시간이 된 요청들을 수집
        count = 0
        for i in range(pos, len(jobs)):
            if jobs[i][0] <= time:
                heapq.heappush(waits,(jobs[i][1],jobs[i][0]))
                count += 1
            else:
                break
        pos += count
        # 여기까지 수집하는 과정

        # 대기 list에 들어와서 실질적으로 처리해야되는 task들
        if waits:
            temp = heapq.heappop(waits)
            time += temp[0]
            answer += time - temp[1]
        else:
            time += 1
        # 하나 처리 완료

    return int(answer/len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))

