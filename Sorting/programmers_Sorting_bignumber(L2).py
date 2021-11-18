def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# 간단한 sort 문제라고 생각했지만 생각보다 조건이 까다로웠던 문제
# str로 sort를 하면 순서대로 원하는대로 정렬은 되지만,
# lambda x: x*3를 해주는게 포인트
# 숫자의 크기가 0~1000이므로 앞의 세개를 비교해주는 식으로