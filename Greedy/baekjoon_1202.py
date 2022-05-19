import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewelry = []
bag = []

for i in range(n):
    weight, price = map(int, sys.stdin.readline().split())
    heapq.heappush(jewelry, (weight, price))

for i in range(k):
    heapq.heappush(bag, int(sys.stdin.readline()))

result = 0
tmp_bag = []
for _ in range(k):
    bag_w = heapq.heappop(bag)

    while jewelry and bag_w >= jewelry[0][0]:
        heapq.heappush(tmp_bag, -heapq.heappop(jewelry)[1])

    if tmp_bag:
        result -= heapq.heappop(tmp_bag)

    elif not jewelry and tmp_bag:
        break

print(result)