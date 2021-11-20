import math
m, n = map(int, input().split())
for i in range(m, n+1):
    evidence = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            evidence += 1
            break
    if evidence == 0 and i != 1:
        print(i)