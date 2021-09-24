import sys

t = int(sys.stdin.readline())
case = list()
for i in range(t):
    case.append(int(sys.stdin.readline()))

arr = [0] * 101
arr[1:10] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, max(case)+1):
    arr[i] = arr[i-1] + arr[i-5]

for i in case:
    print(arr[i])