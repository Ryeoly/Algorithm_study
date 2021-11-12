number = int(input())
arr = [[0 for i in range(15)] for i in range(15)]
arr[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

for i in range(number):
    k = int(input())
    n = int(input())

    for p in range(1,k+1):
        for q in range(n):
            arr[p][q] = sum(arr[p-1][:q+1])
    print(arr[k][n-1])