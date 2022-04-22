import sys

n = int(sys.stdin.readline())
arr = list()
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

result = 0
pre_time = 0
for times in arr:
    if pre_time <= times[0]:
        pre_time = times[1]
        result += 1
print(result)