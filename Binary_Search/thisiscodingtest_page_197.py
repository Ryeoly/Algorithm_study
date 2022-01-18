import sys

def binary_search(objes, number, n):
    start = 0
    end = n-1

    while start <= end:
        mid = int((start + end) // 2)
        if objes[mid] == number:
            return "yes"
        elif objes[mid] < number:
            start = mid+1
        else:
            end = mid-1

    return "no"

answer = list()
n = int(sys.stdin.readline())
objes = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
want = list(map(int, sys.stdin.readline().split()))

objes.sort()

for i in want:
    answer.append(binary_search(objes, i, n))

print(" ".join(answer))