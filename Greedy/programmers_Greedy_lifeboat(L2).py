def solution(people, limit):
    answer = 0

    people.sort()

    start = 0
    end = len(people)-1

    while start <= end: # 같은 경우는?
        if start != end and people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

# case 1 (효율성 1, 3 통과가 안됨)
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     order = [i for i in range(len(people))]
#
#     while order:
#         select_person = order.pop()
#
#         minvalue = 9999999
#         number = -1
#
#         for i in order:
#             temp = limit - (people[i] + people[select_person])
#             if 0 <= temp < minvalue:
#                 minvalue = temp
#                 number = i
#             elif temp <= 0:
#                 break
#
#         if number != -1:
#             order.remove(number)
#
#         answer += 1
#
#     return answer
