x = list()
y = list()
result = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(3):
    if x.count(x[i]) != 2:
        result.append(x[i])
        break
for i in range(3):
    if y.count(y[i]) != 2:
        result.append(y[i])
        break
print(result[0], result[1])