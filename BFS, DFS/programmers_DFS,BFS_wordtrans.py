from collections import deque

def count(word, want):
    count = 0
    for i in range(len(word)):
        if word[i] != want[i]:
            count += 1
    return count

def solution(begin, target, words):
    answer = 0

    try:
        words.index(target)
    except:
        return 0

    arr = deque()
    arr.append((begin, begin, 0))

    while arr:
        pre_word, cur_word, counting = arr.popleft()
        if cur_word == target:
            answer = counting
            break

        for i in words:
            if i == cur_word or i == pre_word:
                continue
            else:
                dif = count(i, cur_word)
                if dif == 1:
                    arr.append((cur_word, i, counting+1))
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log","cog"]
print(solution(begin, target, words))