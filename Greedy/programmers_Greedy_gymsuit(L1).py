def solution(n, lost, reserve):
    arr = [1] * (n + 1)

    for i in range(1, n + 1):
        if i in lost:
            arr[i] -= 1
        if i in reserve:
            arr[i] += 1

    for i in range(1, n + 1):
        if arr[i] == 0 and arr[i - 1] == 2:
            arr[i - 1] -= 1
            arr[i] += 1

        elif arr[i] == 0 and i < n and arr[i + 1] == 2:
            arr[i + 1] -= 1
            arr[i] += 1

    return n - arr.count(0)