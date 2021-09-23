import sys

n = int(sys.stdin.readline())
arr = [0]*1000001
arr[0] = 0
arr[1] = 1
arr[2] = 2
for i in range(3, n+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 15746
print(arr[n])

# arr 초기화를 [0]*n+1로 진행했을 경우 n=1일 때 arr[2]라는
# 값이 존재하지 않아 런타임 에러가 7번째 줄에서 뜨게 된다.
# n+를 더 해주던가, 위처럼 n의 범위를 생각해서 배열을 다 만들어주던가
# 결정하여 진행해야 한다.