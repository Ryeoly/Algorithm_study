from collections import deque
def check(a, b, c, d, n, number):
    if (a == n - 1 and b == n - 1) or (c == n - 1 and d == n - 1):
        return number + 1
    return 0

def add(a, b, c, d, que, evidence, number,n):
    temp = check(a,b,c,d,n, number)
    if temp > 0:
        return True, temp
    que.append(((a, b), (c, d), number + 1))
    evidence.append(((a,b), (c,d)))
    return False, temp

def solution(board):
    answer = 0
    n = len(board)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    que = deque()
    que.append(((0,0), (0,1), 0))

    # 이동했던 곳엔 다시 못오게 하려고, 뺑뺑이를 돌지 못하게 하려고
    evidence = list()
    evidence.append(((0,0), (0,1)))

    while que:
        left, rigth, number = que.popleft()
        a, b = left[0], left[1]
        c, d = rigth[0], rigth[1]

        # 상하좌우 이동
        for i in range(4):
            t_a, t_b = a + dx[i], b + dy[i]
            t_c, t_d = c + dx[i], d + dy[i]

            if 0 <= t_a < n and 0 <= t_b < n and 0 <= t_c < n and 0 <= t_d < n:
                if board[t_a][t_b] == 0 and board[t_c][t_d] == 0 and ((t_a, t_b), (t_c, t_d)) not in evidence:
                    t = add(t_a,t_b, t_c, t_d, que, evidence, number,n)
                    if t[0]:
                        return t[1]

        # 90도 이동
        if a == c and b + 1 == d: # 가로로 놓인 경우
            if 0 <= a-1 < n and 0 <= b+1 < n and  0 <= c-1 < n and 0 <= d-1 < n and board[a-1][b+1] == 0 and board[c-1][d-1] == 0: # 위쪽이 둘다 빈 경우
                if ((c - 1, d - 1), (a, b)) not in evidence:
                    t = add(c-1, d-1, a, b, que, evidence, number,n)
                    if t[0]:
                        return t[1]

                if ((a - 1, b + 1), (c, d)) not in evidence:
                    t = add(a-1, b+1, c, d, que, evidence, number,n)
                    if t[0]:
                        return t[1]

            if 0 <= a+1 < n and 0 <= b+1 < n and 0 <= c+1 < n and 0 <= d-1 < n and board[c+1][d-1] == 0 and board[a+1][b+1] == 0: # 아래가 둘다 빈 경우
                if ((c, d), (a + 1, b + 1)) not in evidence:
                    t = add(c, d, a+1, b+1, que, evidence, number,n)
                    if t[0]:
                        return t[1]

                if ((a, b), (c + 1, d - 1)) not in evidence:
                    t = add(a, b, c+1, d-1, que, evidence, number,n)
                    if t[0]:
                        return t[1]

        elif a+1 == c and b == d: # 세로로 놓인 경우
            if 0 <= a + 1 < n and 0 <= b - 1 < n and 0 <= c - 1 < n and 0 <= d - 1 < n and board[a + 1][b - 1] == 0 and board[c-1][d-1] == 0:
                if ((c - 1, d - 1), (a, b)) not in evidence:
                    t = add(c-1, d-1, a, b, que, evidence, number,n)
                    if t[0]:
                        return t[1]

                if ((a + 1, b - 1), (c, d)) not in evidence:
                    t = add(a+1, b-1, c, d, que, evidence, number,n)
                    if t[0]:
                        return t[1]

            if 0 <= a + 1 < n and 0 <= b + 1 < n and 0 <= c - 1 < n and 0 <= d + 1 < n and board[a + 1][b + 1] == 0 and board[c-1][d+1] == 0:
                if ((a, b), (c - 1, d + 1)) not in evidence:
                    t = add(a, b, c-1, d+1, que, evidence, number,n)
                    if t[0]:
                        return t[1]

                if ((c, d), (a + 1, b + 1)) not in evidence:
                    t = add(c, d, a+1, b+1, que, evidence, number,n)
                    if t[0]:
                        return t[1]

    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
