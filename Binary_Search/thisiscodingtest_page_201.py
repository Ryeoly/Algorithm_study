import sys

n, m = map(int, sys.stdin.readline().split())
cakes = list(map(int, sys.stdin.readline().split()))

def b_s(cakes, start, end, m):

    while start <= end:
        cake_cm = 0
        mid = int((start + end)//2)
        for i in cakes:
            if i > mid :
                cake_cm += i-mid

        if cake_cm == m:
            return mid
        elif cake_cm < m:
            end = mid-1
        else:
            start = mid+1

    return int((start + end)//2)

cakes.sort()
print(b_s(cakes, 0, cakes[-1], m))