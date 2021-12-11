import heapq


def solution(operations):
    min_h = list()
    max_h = list()
    count = 0

    for i in operations:
        temp = i.split(" ")
        if temp[0] == "I":
            heapq.heappush(min_h, int(temp[1]))
            heapq.heappush(max_h, -1 * int(temp[1]))
            count += 1

        elif temp[0] == "D" and count > 0:
            count -= 1
            if int(temp[1]) == 1 and max_h:
                heapq.heappop(max_h)
            elif int(temp[1]) == -1 and min_h:
                heapq.heappop(min_h)


        if count <= 0:
            max_h.clear()
            min_h.clear()


    if max_h and min_h:
        max = -1 * heapq.heappop(max_h)
        min = heapq.heappop(min_h)

        if max < min:
            return [0, 0]
        else:
            return [max, min]
    else:
        return [0,0]
#
# print(solution(["I 16","D 1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
