def exec(arr, n):
    result = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            result[y][n-x-1] = arr[x][y]

    return result

t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(str, input().split())))

    first = exec(arr, n)
    second = exec(first, n)
    third = exec(second, n)

    print("#"+str(i+1))
    for p in range(n):
        line = ""
        line += ''.join(first[p])
        line += " "
        line += ''.join(second[p])
        line += " "
        line += ''.join(third[p])
        print(line)


