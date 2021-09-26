import sys

def find_number(start, end, number, arr):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == number:
            return 1
        elif arr[mid] < number:
            start = mid+1
        elif arr[mid] > number:
            end = mid-1
    return 0


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

arr.sort()
for i in find:
    print(find_number(0,n-1, i, arr))