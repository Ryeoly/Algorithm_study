def line_g(arr):

    for i in range(9):
        check = [0] * 9
        for j in range(9):
            check[arr[i][j]-1] += 1
        if check != [1]*9:
            return False
    return True

def line_s(arr):
    for i in range(9):
        check = [0] * 9
        for j in range(9):
            check[arr[j][i]-1] += 1
        if check != [1] * 9:
            return False
    return True

def check_arr(arr):
    for i in range(3):
        for j in range(3):
            check = [0] * 9
            for x in range(3):
                for y in range(3):
                    check[arr[x+3*i][y+3*j]-1] += 1
            if check != [1]*9:
                return False
    return True

t = int(input())
for i in range(t):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    if line_g(arr) and line_s(arr) and check_arr(arr):
        print("#" + str(i + 1) + " " + str(1))
    else:
        print("#" + str(i + 1) + " " + str(0))