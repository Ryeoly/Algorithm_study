from collections import deque

k, n = map(int, input().split())
queue = deque(i for i in range(1, k+1))
result = list()
number = 0
dele = list()
while queue:
    number += n
    while number > len(queue) and queue:
        number = number-len(queue)
        if dele:
            for j in dele:
                queue.remove(j)
            dele.clear()
    try:
        dele.append(queue[number-1])
    except:
        continue
    result.append(queue[number-1])
print('<'+', '.join(map(str, result))+'>')