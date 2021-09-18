n, m = map(int, input().split())
tree = list(map(int, input().split()))


def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        distance = sum(i-mid if i>mid else 0 for i in tree)

        if distance < m:
            end = mid - 1
        elif distance >= m:
            start = mid + 1
            result = mid
    return result


print(binary_search(0, max(tree)))