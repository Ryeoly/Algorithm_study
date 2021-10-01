import sys
n, k = map(int, sys.stdin.readline().split())
arr = list()
count = 0

for i in range(n):
    arr.append(int(sys.stdin.readline()))

for j in arr[::-1]:
    count += k//j
    k = k%j
print(count)