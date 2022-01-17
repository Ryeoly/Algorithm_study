def solution(routes):
    answer = 0

    arr = list()

    routes = sorted(routes, key=lambda x: x[0])

    answer += 1
    arr.append(routes[0])

    for i in range(1, len(routes)):
        start, end = routes[i][0], routes[i][1]
        pre_start, pre_end = arr[-1][0], arr[-1][1]

        if pre_start <= start <= pre_end <= end:
            arr.pop()
            arr.append([start, pre_end])
        elif pre_start <= start <= end <= pre_end:
            arr.pop()
            arr.append([start, end])
        else:
            answer += 1
            arr.append(routes[i])

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))