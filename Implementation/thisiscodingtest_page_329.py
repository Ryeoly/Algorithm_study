def possible(answer):
    for i in answer:
        x, y, a = i
        if a == 0:
            if y == 0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False

        elif a == 1:
            if ([x-1, y, 1] in answer and [x+1, y, 1] in answer) or [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for i in build_frame:
        x, y, a, b = i

        if b == 0:
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])

        elif b == 1:
            answer.append([x,y,a])
            if not possible(answer):
                answer.remove([x,y,a])
    return sorted(answer)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))