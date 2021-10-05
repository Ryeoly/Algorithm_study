import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i]+arr[i-1])
print(max(arr))

# 트리 형태로 쭉 연속된 합이 내려가게 된다.
# 고민하던 이유는 1 -> 1+2, 2 -> 1+2+3, 2+3, 3 -> 1+2+3+4, 2+3+4, 3+4, 4...으로
# 트리 형태로 늘어가는 것들을 어떻게 기록할 건지 대한 부분인데
# 아주 간단하게 해결할 수 있었다.
# ! 연속된 합 중 최대 값을 i-1에 기록한 것이기 때문에 항상 두개만 비교해도 문제가 되지 않는다.
