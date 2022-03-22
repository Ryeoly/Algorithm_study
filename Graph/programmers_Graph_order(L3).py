# def solution(n, results):
#     answer = 0
#     INF = int(1e9)
#     arr = [[INF]*n for _ in range(n)]
#
#     for result in results:
#         x, y = result[0], result[1]
#         arr[x-1][y-1] = 1
#
#     for i in range(n):
#         arr[i][i] = 0
#
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
#
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] != INF and arr[i][j] != 0 and arr[j][i] == INF:
#                 arr[j][i] = arr[i][j]
#
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[i][j] == INF:
#                 count += 1
#         if count == 0:
#             answer += 1
#
#     return answer
#
# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# code review
def solution(n, results):
    answer = 0
    arr = [["?"]*n for _ in range(n)]

    for result in results:
        arr[result[0]-1][result[1]-1] = "WIN"
        arr[result[1] - 1][result[0] - 1] = "LOSE"

    for i in range(n):
        arr[i][i] = "ME"

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][k] == "WIN" and arr[k][j] == "WIN":
                    arr[i][j] = "WIN"
                elif arr[i][k] == "LOSE" and arr[k][j] == "LOSE":
                    arr[i][j] = "LOSE"

    for i in arr:
        if "?" not in i:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))