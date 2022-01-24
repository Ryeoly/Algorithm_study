# 내가 짠 간단한 코드
n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] != arr[j]:
            count += 1

print(count)

# 이코테에 적힌 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))
arr = [0] * 11

for i in data:
    arr[i] += 1

count = 0
for i in range(1, m+1):
    n -= arr[i]
    count += arr[i]*n

print(count)