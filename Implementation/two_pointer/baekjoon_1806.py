n, want = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
s = 0
result = int(1e9)+2

for start in range(n):
    while s < want and end < n:
        s += arr[end]
        end += 1
    if s >= want:
        result = min(result, end-start)
    s -= arr[start]

if result == int(1e9)+2:
    print(0)
else:
    print(result)