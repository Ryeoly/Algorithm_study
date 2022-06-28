import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr_set = set(arr)

gar_set = set()
result = 0

for i in arr:
    need_num = x - i
    if i in gar_set or need_num in gar_set or ((x % 2) == 0 and x//2 == i):
        continue

    if need_num in arr_set:
        result += 1
        gar_set.add(i)
        gar_set.add(need_num)

print(result)

