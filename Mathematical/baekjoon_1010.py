import math
import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    result = math.factorial(m) / (math.factorial(n)*math.factorial(m-n))
    print(int(result))