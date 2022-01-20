# 내가 짠 코드
def check(arr):
    n = len(arr)
    for i in arr:
        if i > n:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))
pos = 0
answer = 0
arr.sort()

while pos < n:
    if check(arr[pos:pos+arr[pos]]):
        pos += arr[pos]
        answer += 1
    else:
        pos += 1

print(answer)

# 답지 코드
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)