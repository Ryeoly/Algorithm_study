import math
n = int(input())
arr = list(map(int, input().split()))
first = arr[0]
for i in arr[1:]:
    gcd = math.gcd(first, i)
    print("{}/{}".format(int(first/gcd),int(i/gcd) ))