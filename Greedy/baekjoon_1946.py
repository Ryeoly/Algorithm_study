# import sys
#
# t = int(sys.stdin.readline())
# for i in range(t):
#     n = int(sys.stdin.readline())
#     arr = []
#     for j in range(n):
#         arr.append(list(map(int, sys.stdin.readline().split())))
#     arr.sort(key=lambda x:(x[0],x[1]))
#
#     result = 0
#     value = int(1e9)
#     for p in range(n):
#         if arr[p][1] < value:
#             result += 1
#             value = arr[p][1]
#     print(result)

#### 위엔 sort를 해서 처음 순위가 낮은 애들부터 비교해 후자 순위 min값과 비교하는 알고리즘
#### 밑엔 sort를 하지 않고, 애초에 arr[처음 순위] = [후자 순위]로 list를 만들어 sort를 하지 않아도 되도록 함
import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    arr = [0] * (n+1)
    for j in range(n):
        x, y = map(int, sys.stdin.readline().split())
        arr[x] = y

    arr[0] = 1
    value = arr[1]
    for p in range(2, n+1):
        if arr[p] < value:
            arr[0] += 1
            value = arr[p]
    print(arr[0])