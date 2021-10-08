import sys

n = int(sys.stdin.readline())
for i in range(n):
    line = list(map(str,sys.stdin.readline().rstrip()))
    right = 0
    left = 0
    for j in line:
        if j == "(":
            left += 1
        elif j == ")":
            right += 1
        if right > left:
            break
    if right != left:
        print("NO")
    else:
        print("YES")