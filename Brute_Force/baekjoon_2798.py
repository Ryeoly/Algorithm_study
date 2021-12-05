import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = list(itertools.combinations(arr, 3))
sum_num = 0
min_num = 100000000000
for i in result:
    if 0 <= m-sum(i) < min_num:
        min_num = m-sum(i)
        sum_num = sum(i)
print(sum_num)