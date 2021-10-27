import sys
import math
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for i in arr:
    count = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            count += 1
    if count == 0:
        result += 1
if 1 in arr:
    result -= 1
print(result)