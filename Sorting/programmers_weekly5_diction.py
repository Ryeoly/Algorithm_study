word = "AAAAE"
result = 6

def solution(word):
    sample = ["A", "E", "I", "O", "U"]
    arr = list()
    arr_2 = list()
    arr_3 = list()
    arr_4 = list()
    arr_5 = list()

    for i in sample:
        arr.append(i)
    arr_2 = make_arr(arr, sample)
    arr_3 = make_arr(arr_2, sample)
    arr_4 = make_arr(arr_3, sample)
    arr_5 = make_arr(arr_4, sample)

    result = arr + arr_2 + arr_3 + arr_4 + arr_5
    result.sort()
    answer = result.index(word)+1

    return answer


def make_arr(arr, sample):
    next_arr = list()
    for i in arr:
        for j in sample:
            temp = i + j
            next_arr.append(temp)
    return next_arr

print(solution(word))