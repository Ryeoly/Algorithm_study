import sys

def check(arr, dis):
    cur = arr[0]
    result = 1
    for i in range(1, len(arr)):
        if arr[i] - cur >= dis:
            result += 1
            cur = arr[i]

    return result


def binary_search(start, end, arr, c):
    while start <= end:
        mid = (start + end) // 2

        number = check(arr, mid)
        if number < c:
            end = mid - 1
        else:
            start = mid + 1

    return (start+end) // 2


n, c = map(int, sys.stdin.readline().split())
arr = list()
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print(binary_search(1, arr[-1]-arr[0], arr, c))
