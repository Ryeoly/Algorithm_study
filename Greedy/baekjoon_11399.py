n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
re = list()
for i in arr:
    result += i
    re.append(result)
print(sum(re))