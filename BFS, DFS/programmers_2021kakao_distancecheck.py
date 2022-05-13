def first_check(arr, o_pos):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    for o in o_pos:
        x, y = o[0], o[1]
        count = 0
        for i in range(4):
            t_x, t_y = x+dx[i], y+dy[i]
            if 0 <= t_x <= 4 and 0 <= t_y <= 4 and arr[t_x][t_y] == "P":
                count += 1
        if count >= 2:
            return False

    return True

def second_check(arr, p_pos):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    for p in p_pos:
        x, y = p[0], p[1]
        for i in range(4):
            t_x, t_y = x + dx[i], y + dy[i]
            if 0 <= t_x <= 4 and 0 <= t_y <= 4 and arr[t_x][t_y] == "P":
                return False
    return True

def solution(places):
    answer = []

    for place in places:
        p_pos = []
        o_pos = []
        arr = []
        for i in range(5):
            arr.append(list(place[i]))

        for i in range(5):
            for j in range(5):
                if arr[i][j] == "P":
                    p_pos.append([i, j])
                elif arr[i][j] == "O":
                    o_pos.append([i, j])

        if first_check(arr, o_pos):
            if second_check(arr, p_pos):
                answer.append(1)
            else:
                answer.append(0)
        else:
            answer.append(0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))