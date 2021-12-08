def count(word, want):
    count = 0
    for i in range(len(word)):
        if word[i] != want[i]:
            count += 1

    return count


def solution(begin, target, words):
    answer = 0
    a = words.index(target)
    pos = 0
    while pos < len(words):
        dif = count(begin, target)
        if dif == 1:
            answer += 1
            break
        trans_dif = count(begin, words[pos])
        if trans_dif != 1:
            return 0
        else:
            begin = words[pos]
            pos += 1
            answer += 1

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))