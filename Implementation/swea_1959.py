def cal(arr, brr, a_len, b_len, flag):
    result = list()
    if flag:
        for i in range(b_len-a_len+1):
            temp = 0
            for j in  range(a_len):
                temp += arr[j]*brr[j+i]
            result.append(temp)
    else:
        for i in range(a_len - b_len + 1):
            temp = 0
            for j in range(b_len):
                temp += arr[j+i] * brr[j]
            result.append(temp)
    return max(result)


t = int(input())

for i in range(t):
    a_len, b_len = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    result = 0
    if a_len <= b_len:
        result = cal(arr, brr, a_len, b_len, True)
    elif b_len < a_len:
        result = cal(arr, brr, a_len, b_len, False)
    else:
        print("err")
        break

    print("#"+str(i+1)+" "+str(result))