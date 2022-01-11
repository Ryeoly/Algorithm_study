def solution(number, k):
    answer = list()
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return "".join(answer[:len(answer)-k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("888899", 3))


# def check(number):
#     max_number = 0
#     max_index = 0
#     for index, value in enumerate(number):
#         if value > max_number:
#             max_number = value
#             max_index = index
#         if max_number == 9:
#             break
#     return max_number, max_index
#
#
# def solution(number, k):
#     answer = list()
#     number = list(map(int, number))
#     pos = 0
#
#     while k>0:
#         temp = number[pos:pos+k+1]
#
#         max_number, max_index = check(temp)
#
#         answer.append(max_number)
#         k -= max_index
#         pos += max_index+1
#
#     if pos < len(number):
#         answer = answer + number[pos:]
#
#     return "".join(list(map(str,answer)))
#
# print(solution("1924", 2))
# print(solution("1231234", 3))
# print(solution("4177252841", 4))
# print(solution("888899", 3))
