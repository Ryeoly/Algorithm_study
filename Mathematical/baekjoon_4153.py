while 1:
    index = [0,1,2]
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    index.remove(arr.index(max(arr)))
    index.remove(arr.index(min(arr)))
    if max(arr)*max(arr) == min(arr)*min(arr) + arr[index[0]]*arr[index[0]]:
        print("right")
    else:
        print("wrong")