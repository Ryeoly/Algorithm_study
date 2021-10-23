import sys

while 1:
    first, second = map(int, sys.stdin.readline().split())

    if first == 0 and second == 0:
        break

    if first <= second and second%first == 0:
        print("factor")
    elif second <= first and first%second == 0:
        print("multiple")
    else:
        print("neither")