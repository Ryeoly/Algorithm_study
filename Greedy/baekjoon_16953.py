a, b = map(int, input().split())

result = 1

while 1:
    if a == b:
        break
    if (b % 2 != 0 and b % 10 != 1) or b < a:
        result = -1
        break
    else:
        if b % 2 == 0:
            b //= 2
            result += 1
        else:
            b //= 10
            result += 1

print(result)