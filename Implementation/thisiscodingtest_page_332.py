import itertools

N, M = map(int, input().split())
arr = list()
home = list()
chicken = list()

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])

combi = list(itertools.combinations(chicken, M))

results = list()
for i in combi:
    dis = 0
    for q in home:
        mini = int(1e9)
        for j in i:
            distance = abs(j[0]-q[0])+abs(j[1]-q[1])
            if distance < mini:
                mini = distance
        dis += mini
    results.append(dis)

print(min(results))