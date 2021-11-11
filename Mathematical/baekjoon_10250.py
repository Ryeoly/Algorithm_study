import sys

n = int(sys.stdin.readline())
for i in range(n):
    h, w, n = map(int, sys.stdin.readline().split())
    width = int(n // h) + (1 if n%h>0 else 0)
    height = (h if n%h==0 else int(n % h))
    print(str(height)+str(width).zfill(2))