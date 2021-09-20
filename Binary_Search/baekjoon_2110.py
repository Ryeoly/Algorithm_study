import sys

n, c = map(int, sys.stdin.readline().split())
arr = list()
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end)//2
        count = check(mid)
        if count < c:
            end = mid - 1
        else:
            start = mid + 1
            result = mid
    return result

def check(dis):
    count = 1
    pre = arr[0]
    for i in arr:
        if i - pre >= dis:
            count += 1
            pre = i
    return count

if c == 2:
    print(max(arr) - min(arr))
else:
    print(binary_search(1, max(arr)))

# "가장 인접한 두 공유기 사이의 거리를 최대"라는 문장에 사로 잡혀 이해를 제대로 하지 못한 문제
# 단순히 주어진 위치 안에서 공유기를 최대로 놓을 수 있는 거리를 구하면 되는 문제.
# 좌표가 10억이라는 큰 수로 주어졌기에 좌표를 binary로 줄여나가라는 힌트를 간접적으로 주었고
# 좀더 넓은 시야로 보는 능력을 길러야 한다는 것을 느낌