def check(pos):
    for i in range(pos):
        if board[pos] == board[i] or (pos-i == abs(board[pos] - board[i])):
            return False
    return True

def execut(depth, n):
    if depth == n:
        global result
        result += 1
        return

    else:
        for i in range(n):
            board[depth] = i
            if check(depth):
                execut(depth+1, n)
    return

n = int(input())
board = [0] * n
result = 0
execut(0, n)

print(result)