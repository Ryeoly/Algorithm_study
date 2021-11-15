def solution(genres, plays):
    answer = []
    diction = dict()
    number = dict()

    for i in range(len(genres)):
        try:
            diction[genres[i]] += plays[i]
            temp = number[genres[i]].copy()
            temp.append((i, plays[i]))
            number[genres[i]] = temp.copy()
        except:
            diction[genres[i]] = plays[i]
            number[genres[i]] = [(i, plays[i])]

    dictions = sorted(diction.items(), key=lambda item: item[1], reverse=True)


    for i in dictions:
        temp = number[i[0]].copy()
        temp.sort(key=lambda item:item[1], reverse=True)
        if len(temp) == 1 :
            answer.append(temp[0][0])
        else:
            for j in range(2):
                answer.append(temp[j][0])


    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

# 문제만 이해한다면 어렵지 않게 풀수 있는 알고리즘