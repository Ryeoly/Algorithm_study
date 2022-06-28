n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n-1
pre = int(1e9)*2
result = []

while left < right:
    cur = arr[left] + arr[right]

    if abs(cur) < pre:
        pre = abs(cur)
        result = [arr[left], arr[right]]

    if cur < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])