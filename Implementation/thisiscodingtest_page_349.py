import sys
import itertools

def cal(sign, first, second):
    if sign == "+":
        return first+second
    elif sign == "-":
        return first-second
    elif sign == "*":
        return first*second
    else:
        if first > 0:
            return first//second
        elif first == 0:
            return 0
        else:
            return -1 * ((-1*first)//second)

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
signs = list(map(int, sys.stdin.readline().split()))
s_signs = list()

for i in range(signs[0]):
    s_signs.append("+")
for i in range(signs[1]):
    s_signs.append("-")
for i in range(signs[2]):
    s_signs.append("*")
for i in range(signs[3]):
    s_signs.append("%")

ss_signs = list(set(itertools.permutations(s_signs, sum(signs))))

result = [numbers[0]] * len(ss_signs)

for i in range(1, n):
    temp = numbers[i]
    for j in range(len(ss_signs)):
        result[j] = cal(ss_signs[j][i-1], result[j], temp)

print(max(result))
print(min(result))