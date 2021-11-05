def solution(clothes):
    diction = dict()
    for i in clothes:
        try:
            diction[i[1]] += 1
        except:
            diction[i[1]] = 2

    result = 1
    for i in diction.keys():
        result *= diction[i]

    return result - 1

# 백준에서 동일한 문제를 풀어봤기에 간단히 해결했다.