import sys
import math
def count(number):
    if number == 1:
        return 1
    arr = list()
    for i in range(number+1, number*2+1):
        evidence = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                evidence = 1
                break
        if evidence == 0:
            arr.append(i)
    return len(arr)

while 1:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    print(count(n))