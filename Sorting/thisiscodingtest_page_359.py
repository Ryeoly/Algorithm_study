import sys

arr = list()
n = int(sys.stdin.readline())

for i in range(n):
    name, kor, en, math = sys.stdin.readline().split()

    arr.append([name, int(kor), int(en), int(math)])

result = sorted(arr, key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(result[i][0])

