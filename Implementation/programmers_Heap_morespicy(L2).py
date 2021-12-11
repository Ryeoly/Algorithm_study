import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        number = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, number)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))