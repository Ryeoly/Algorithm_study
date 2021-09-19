import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))

result = 0
mini_cost = 999999999999999999999999999999999
for i in range(n-1):
    if city[i] < mini_cost:
        mini_cost = city[i]
    result += mini_cost*distance[i]
print(result)