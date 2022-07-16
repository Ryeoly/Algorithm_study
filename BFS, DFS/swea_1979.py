def check(arr, n, k):
    result = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(n+2):
        for j in range(n+2):
            if arr[i][j] == 0:
                for p in range(4):
                    temp = 1
                    while 1:
                        tx, ty = i + dx[p]*temp, j + dy[p]*temp
                        if 0 <= tx < n+2 and 0 <= ty < n+2 and arr[tx][ty] == 1:
                            temp += 1
                        else:
                            break
                    if temp-1 == k:
                        result += 1

    return result//2


t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    arr = list()
    arr.append([0]*(n+2))
    for j in range(n):
        temp = [0]
        temp += list(map(int, input().split()))
        temp += [0]
        arr.append(temp)
    arr.append([0] * (n+2))

    result = check(arr, n, k)
    print("#"+str(i+1)+" "+str(result))
