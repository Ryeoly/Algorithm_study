from collections import deque
def solution(tickets):
    answer = ["ICN"]

    arr = deque()
    arr.append([tickets, answer])

    while arr:
        order = arr.popleft()
        _tickets, _answer = order[0], order[1]

        if len(_tickets) == 0:
            answer.append(_answer)

        for ticket in _tickets:
            if _answer[-1] == ticket[0]:
                temp = _tickets.copy()
                temp.remove(ticket)

                temp2 = _answer.copy()
                temp2.append(ticket[1])
                arr.append([temp, temp2])

    answer.remove("ICN")
    answer.sort()
    for i in answer:
        if len(i) == len(tickets)+1:
            return i

    return 0

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
