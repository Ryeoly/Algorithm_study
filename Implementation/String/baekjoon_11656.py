s = input()
result = list()
for i in range(len(s)):
    result.append(s[i:])

result.sort()
print('\n'.join(result))