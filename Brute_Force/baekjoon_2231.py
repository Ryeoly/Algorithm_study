n = int(input())

arr = list()
for i in range(1, n):
    div = list(map(int, str(i)))
    if sum(div)+i == n:
        arr.append(i)

print(min(arr) if len(arr)>0 else 0)