def solution(brown, yellow):
    factors = list()
    sum = brown + yellow
    for i in range(1, int((sum + 1) ** (1 / 2)) + 1):
        if sum % i == 0:
            factors.append((i, int(sum / i)))

    for factor in factors:
        if brown == 2 * factor[0] + 2 * factor[1] - 4:
            return [factor[1], factor[0]]

print(solution(10,2))