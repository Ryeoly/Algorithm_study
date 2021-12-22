import sys
import math

def check(n): # 소수가 아니면 False, 소수면 True
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    
    half = int(n/2)
    _half = half

    while 1:
        if check(half) and check(_half):
            print(half, _half)
            break
        half-=1
        _half+=1
