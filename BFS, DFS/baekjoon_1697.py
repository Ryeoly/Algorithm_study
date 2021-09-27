from collections import deque


def bfs(n, k, arr):
    queue = deque()
    arr[n] = 0
    queue.append(n)
    while 1:
        pos = queue.popleft()
        if pos == k:
            break
        if 0 <= (pos+1) <= 1000000 and arr[pos+1] == -1:
            arr[pos+1] = arr[pos]+1
            queue.append(pos+1)
        if 0 <= (pos-1) <= 1000000 and arr[pos-1] == -1:
            arr[pos-1] = arr[pos]+1
            queue.append(pos-1)
        if 0 <= 2*pos <= 1000000 and arr[2*pos] == -1:
            arr[2*pos] = arr[pos]+1
            queue.append(2*pos)
        else:
            continue
    return arr


n, k = map(int, input().split())
arr = [-1] * 1000001
if n >= k:
    print(n-k)
else:
   print(bfs(n, k, arr)[k])

# queue를 통해 방문 과정을 순차적으로 진행함으로 앞에 방문해서 -1이 아닌
# 방문된 list는 최소 횟수로 방문을 진행되었다고 판단한다.
# 따라서 -1인 list 위치만 검토해서 횟수를 입력해 준다.