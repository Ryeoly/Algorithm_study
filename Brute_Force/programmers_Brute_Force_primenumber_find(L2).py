from itertools import permutations
def check_num(number):
    if number < 2:
        return False

    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answers = set()
    for i in range(1, len(numbers) + 1):
        samples = set(map(''.join, permutations(list(numbers), i)))
        for sample in samples:
            if check_num(int(sample)):
                answers.add(int(sample))
    return len(answers)

print(solution("011"))