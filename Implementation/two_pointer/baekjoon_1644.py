import math
n = int(input())
numbers = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if numbers[i]:
        j = 2
        while i*j <= n:
            numbers[i*j] = False
            j += 1

arr = []
for i in range(2, n+1):
    if numbers[i]:
        arr.append(i)

result = 0
end = 0
s = 0
for start in range(len(arr)):
    while s < n and end < len(arr):
        s += arr[end]
        end += 1
    if s == n:
        result += 1
    s -= arr[start]

print(result)