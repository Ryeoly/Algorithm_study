price, money, count, result = 3, 20, 4, 10

def solution(price, money, count):
    sum_count = int(count * (count + 1) / 2)
    result = money - price * sum_count

    if result < 0:
        answer = -1 * result
    else:
        answer = 0

    return answer

print(solution(price,money,count))