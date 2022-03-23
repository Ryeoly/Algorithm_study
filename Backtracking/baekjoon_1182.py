n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def back(idx, sub_sum):
    global answer

    if idx >= n:
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        answer += 1

    back(idx+1, sub_sum)
    back(idx+1, sub_sum - arr[idx])

back(0, 0)
print(answer)