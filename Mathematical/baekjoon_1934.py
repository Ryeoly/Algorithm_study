import sys
import math

t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(int(a*b/math.gcd(a, b)))

# 최대공약수를 구하는 법은 유클리드 호제법을 이용해서 효율적으로 구할 수 있다
# 두 수를 나누어 나머지가 0이 될때까지 작은 수와 다시 나누는 법을 반복해서 실행
# 그렇게 구한 수가 최대 공약수이고, 두수를 곱하고 최대공약수로 나누면 최소공배수를
# 구할 수 있다. 이미 있는 이론을 가지고 알고리즘을 효율적으로 구성하는 법