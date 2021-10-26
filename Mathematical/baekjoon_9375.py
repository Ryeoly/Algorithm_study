import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    dictionary = dict()
    for j in range(n):
        result = 0
        wear, wear_type = map(str, sys.stdin.readline().split())
        try:
            dictionary[wear_type] += 1
        except:
            # 여기서 2를 넣는 이유는 입지 않는 경우의 수를 넣어주기 위함
            dictionary[wear_type] = 2
    count = 1
    for p in dictionary.keys():
        count *= dictionary[p]
    print(count-1)

# 처음 구현한 알고리즘은 itertool을 이용해서 옷의 종류에 맞는
# 중복없는 조합을 모두 생성해 value값들을 곱새 더 해주는 개념을 이용
# 하지만 간단하게 종류별 입을 수 있는 옷을 기준으로 상황들을 곱하면
# 되는 간단한 연산이었다. 복잡하게 구현하려 하지말고 수학적인 개념은
# 최대한 간단하게 규칙을 찾으려 노력하자.