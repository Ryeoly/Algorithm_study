import math

N, K = map(int, input().split())

if K<0 or K>N:
    print(0)
else:
    print(int(math.factorial(N)/(math.factorial(K)*math.factorial(N-K))))