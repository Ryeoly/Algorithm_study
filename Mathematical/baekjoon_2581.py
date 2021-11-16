import math

m = int(input())
n = int(input())
result = list()

for i in range(m, n+1):
    count = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        result .append(i)
if m == 1:
    result.remove(1)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))