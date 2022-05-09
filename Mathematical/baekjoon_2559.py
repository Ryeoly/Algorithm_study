n, k = map(int, input().split())
arr = list(map(int, input().split()))
value = [arr[0]]
result = []

for number in arr[1:]:
    value.append(value[-1]+number)

result.append(value[k-1])
for i in range(1, n-k+1):
    result.append(value[i+k-1]-value[i-1])

print(max(result))