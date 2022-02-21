def check(a, b):
    count = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            count += 1
    return count


a, b = input().split()
if len(a) == len(b):
    print(check(a, b))
else:
    result = list()
    for i in range(len(b)-len(a)+1):
        result.append(check(a, b[i:i+len(a)]))
    print(min(result))