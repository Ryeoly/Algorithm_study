import sys

arr = list()
temp = list()
result = list()
n = int(sys.stdin.readline())
order = [n-i for i in range(n)]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

cur = 0
while 1:
    if cur == n:
        for j in result:
            print(j)
        break
    if len(temp) == 0:
        temp.append(order.pop())
        result.append("+")
    elif arr[cur] == temp[len(temp)-1]:
        temp.pop()
        cur += 1
        result.append("-")
    elif arr[cur] not in order and arr[cur] != temp[len(temp)-1]:
        print("NO")
        break
    elif arr[cur] in temp and arr[cur] != temp[len(temp)-1]:
        print("NO")
        break
    else:
        temp.append(order.pop())
        result.append("+")