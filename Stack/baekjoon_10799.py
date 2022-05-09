arr = list(map(str, input().rstrip()))
count = 0
result = 0
pre = ""
for i in arr:
    if i == "(":
        count += 1
    elif i == ")":
        if pre == "(":
           count -= 1
           result += count
        elif pre == ")":
            count -= 1
            result += 1
    else:
        print("-1")
        break
    pre = i

print(result)