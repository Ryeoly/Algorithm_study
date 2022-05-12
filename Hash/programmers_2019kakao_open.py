def solution(record):
    answer = []
    dic = dict()

    for s in record:
        words = s.split(" ")

        if words[0] != "Leave":
            dic[words[1]] = words[2]
        if words[0] == "Enter":
            answer.append(words[1] + "님이 들어왔습니다.")
        if words[0] == "Leave":
            answer.append(words[1] + "님이 나갔습니다.")

    for i in range(len(answer)):
        name, temp = answer[i].split(" ")
        name = name[:-2]
        answer[i] = dic[name] + "님이 " + temp

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
