import sys
import math
n = int(sys.stdin.readline())
for i in range(n):
    x1,y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    center_dis = (x1 - x2) ** 2 + (y1 - y2) ** 2

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        elif r1 < r2 or r2 < r1:
            print(0)
        else:
            print(-1000)
    elif center_dis < max(r1, r2)**2: #내부에 있는 경우
        if math.sqrt(center_dis)+min(r1,r2) == max(r1, r2):
            print(1)
        elif math.sqrt(center_dis)+min(r1,r2) < max(r1, r2):
            print(0)
        else:
            print(2)
    elif center_dis == max(r1, r2)**2:
        print(2)
    else:
        if r1 + r2 < math.sqrt(center_dis):
            print(0)
        elif r1 + r2 == math.sqrt(center_dis):
            print(1)
        else:
            print(2)