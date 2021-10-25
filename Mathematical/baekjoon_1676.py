import math

n = int(input())
result = list(map(str, str(math.factorial(n))))
count = 0
for i in result[::-1]:
    if int(i) == 0:
        count += 1
    else:
        break
print(count)

# 직접 팩토리얼을 구하지 않고 팩토리얼에서 0이 증가하는 규칙을
# 찾는 방법으로도 접근할 수 있다. 시간 제한을 생각해 푸는 것을 고려