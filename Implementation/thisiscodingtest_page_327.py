from collections import deque

# 뱀을 이동 시키고, 사과가 있다면 꼬리를 안짜르고 없다면 짜른다.
# 사과를 먹는다면 사과를 없앤다.
def move(direct, snake, apple):
    col, row = snake[-1][0], snake[-1][1]
    if direct == "up":
        col -= 1
    elif direct == "down":
        col += 1
    elif direct == "right":
        row += 1
    else:
        row -= 1

    if (col, row) in snake:
        return [],[]

    snake.append((col, row))

    if (col, row) in apple:
        apple.remove((col, row))
    else:# 사과가 없으면 짤라
        snake.popleft()

    return snake, apple

# 직접 초를 계산하며 연산들을 진행
def solution(K, N, apple, L, event):
    direct = ["up", "right", "down", "left"]
    pos = 1
    sec = 0
    snake = deque()
    snake.append((1, 1))

    while 1:
        sec += 1

        snake, apple = move(direct[pos], snake, apple)
        # 몸통에 닿으면 [], []를 반환하도록 해서 바로 종료
        if len(snake) == 0 and len(apple) == 0:
            return sec
        # 경기장 경계에 닿는다면 종료되도록 하는 조건문
        col, row = snake[-1][0], snake[-1][1]
        if col == 0 or col > N or row == 0 or row > N:
            return sec

        # try, except를 쓴 이유는 int(event[0][0])이 event가 null인 경우 에러를 출력하기에
        # try, except를 없애는 방향으로 리팩토링
        # 이동 방향을 결정해주는 부분
        try:
            if sec == int(event[0][0]):
                x, c = event.popleft()
                if c == "D":
                    pos = (pos+1)%4
                elif c == "L":
                    pos = (pos-1)%4
        except:
            continue

N = int(input())
K = int(input())
apple = list()
for i in range(K):
    x, y = map(int, input().split())
    apple.append((x, y))
L = int(input())
event = deque()
for i in range(L):
    x, c = input().split()
    event.append((x, c))

print(solution(K, N, apple, L, event))

# print((-1)%4) 왜 이게 3이 출력?