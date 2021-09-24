n = int(input())
if n == 1:
    print(0)
else:
    arr = [0] * (n+1)

    for i in range(2, n+1):
        arr[i] = arr[i-1] + 1
        if i % 2 == 0:
            arr[i] = min(arr[i], arr[i//2]+1)
        if i % 3 == 0:
            arr[i] = min(arr[i], arr[i//3]+1)
    print(arr[n])

# 1/10 실행 시간으로 정답인 사람들이 존재. 코드를 이해할 필요가 있다.