number = input()
result = int(number[0])

for i in range(1, len(number)):
    temp = int(number[i])
    if result <= 1 or temp <= 1:
        result += temp
    else:
        result *= temp

print(result)
