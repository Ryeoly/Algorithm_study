import sys

n = int(sys.stdin.readline())
arr = list()

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda arr:(arr[0], arr[1]))
for i in range(n):
    print(arr[i][0],arr[i][1])