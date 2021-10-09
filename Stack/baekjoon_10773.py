import sys

n = int(sys.stdin.readline())
arr = list()
for i in range(n):
    number = int(sys.stdin.readline())
    if number != 0:
        arr.append(number)
    else:
        arr.pop()
print(sum(arr))