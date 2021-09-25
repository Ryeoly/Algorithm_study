import sys

dic = dict()
def w(a, b, c):
    if (a,b,c) in dic:
        return dic[(a,b,c)]
    if a <= 0 or b <= 0 or c <= 0:
        dic[(a,b,c)] = 1
        return dic[(a,b,c)]

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if a < b < c:
        dic[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dic[(a,b,c)]
    else:
        dic[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dic[(a,b,c)]

while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))

# 메모이제이션 기법으로 이전에 구한 값들을 바로 출력하는 식