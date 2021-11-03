n, m = map(int, input().split())


def count(number, k):
    count = 0
    while number != 0:
        number = number // k
        count += number
    return count


two = count(n, 2) - count(m, 2) - count(n - m, 2)
five = count(n, 5) - count(m, 5) - count(n - m, 5)
print(min(two, five))

# 매우 힙겹게 푼 문제
# 팩토리얼을 직접 계산하면 용량이 초과된다는 것을 알면서도 접근할 방법을 몰랐던 문제
# 2과 5 두 수의 지수중 작은 수가 0의 개수를 결정하는 부분은 인지하고 있었다.
# 하지만 팩토리얼의 결과를 나누지 않고 숫자 자체를 직접 나누어 지수를 구할 수 있다는 것을 처음 알았다.

# 우선 특정 숫자를 분해하기 위해선, 특정 숫자의 배수를 먼저 거르고, 제곱수를 거르고, 세제곱 수들을 거르는 식으로
# 문제를 접근해야 한다. 이해하는데 많은 시간을 소요한 문제이므로 다시 보도록하자