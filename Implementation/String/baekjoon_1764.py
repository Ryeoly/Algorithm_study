import sys

n, m = map(int, sys.stdin.readline().split())
arr = set()
for i in range(n):
    arr.add(sys.stdin.readline().strip())
result = list()
for i in range(m):
    temp = sys.stdin.readline().strip()
    if temp in arr:
        result.append(temp)

print(len(result))
result.sort()
print("\n".join(result))