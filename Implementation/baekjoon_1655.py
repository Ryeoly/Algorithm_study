import sys
import heapq

n = int(sys.stdin.readline())
min_h = list()
max_h = list()
if n == 1:
    print(int(sys.stdin.readline()))
elif n == 2:
    first = int(sys.stdin.readline())
    print(first)
    second = int(sys.stdin.readline())
    if first <= second:
        print(first)
    else:
        print(second)
else:
    # 최초 숫자는 min쪽에 넣어 기준을 잡아준다.
    first = int(sys.stdin.readline())
    heapq.heappush(min_h, -1*first)
    print(first)

    # 두번째 숫자까지 받아 두 힙에 기준을 잡아준다.
    second = int(sys.stdin.readline())
    if first < second:
        heapq.heappush(max_h, second)
        print(first)
    else:
        heapq.heappush(max_h, heapq.heappop(min_h)*-1)
        heapq.heappush(min_h, second*-1)
        print(second)

    # 위에서 두번을 실행했기에 n-2번 반복
    for _ in range(n-2):
        x = int(sys.stdin.readline())

        if min_h[0]*-1 <= x <= max_h[0]:
            if len(min_h) <= len(max_h):
                heapq.heappush(min_h, x * -1)
            else:
                heapq.heappush(max_h, x)

        elif x < min_h[0]*-1:
            if len(min_h) <= len(max_h):
                heapq.heappush(min_h, x * -1)
            else:
                heapq.heappush(max_h, heapq.heappop(min_h)*-1)
                heapq.heappush(min_h, x * -1)

        elif max_h[0] < x:
            if len(min_h) <= len(max_h):
                heapq.heappush(min_h, heapq.heappop(max_h)*-1)
                heapq.heappush(max_h, x)
            else:
                heapq.heappush(max_h, x)

        if len(min_h) >= len(max_h):
            print(min_h[0]*-1)
        else:
            print(max_h[0])

