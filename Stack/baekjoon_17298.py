import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = list()
stack.append((arr[0],0))
answer = [-1] * n

for i in range(1, n):
    # if stack[-1][0] > arr[i]:
    #     stack.append((arr[i],i))
    # else:
    #     while stack and stack[-1][0] < arr[i]:
    #         temp = stack.pop()
    #         answer[temp[1]] = arr[i]
    #     stack.append((arr[i], i))
    while stack and stack[-1][0] < arr[i]:
        temp = stack.pop()
        answer[temp[1]] = arr[i]
    stack.append((arr[i], i))

print(" ".join(map(str,answer)))

# 사진 자료를 확인