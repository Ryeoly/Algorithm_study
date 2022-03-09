from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    lens = [[] for _ in range(10001)]
    r_lens = [[] for _  in range(10001)]

    for word in words:
        lens[len(word)].append(word)
        r_lens[len(word)].append(word[::-1])

    for i in range(10001):
        lens[i].sort()
        r_lens[i].sort()

    for querie in queries:

        querie_len = len(querie)

        if querie[-1] == "?": # 뒤쪽으로 ?가 붙은 경우
            start = bisect_left(lens[querie_len], querie.replace("?", "a"))
            end = bisect_right(lens[querie_len], querie.replace("?","z"))

        else:
            t_querie = querie[::-1]
            start = bisect_left(r_lens[querie_len], t_querie.replace("?", "a"))
            end = bisect_right(r_lens[querie_len], t_querie.replace("?", "z"))

        answer.append(end-start)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))