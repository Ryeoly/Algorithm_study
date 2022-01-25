s = input()

def make_word(arr, standard):
    pre = arr[:standard]
    count = 1
    result = ""

    # 조건문의 범위는 계산하며 생각
    for i in range(int(len(arr)/standard)):
        next = arr[standard*(i+1):standard*(i+2)]
        if pre == next:
            count += 1
        else:
            if count == 1:
                result = result + "".join(pre)
            else:
                result = result + str(count) + "".join(pre)
            count = 1
            pre = next

    result = result + arr[int(len(arr)/standard)*standard:]
    return result

words = list()
# 밑에서 i는 묶어서 볼 글자의 개수를 의미하게 된다
# 한글자부터 ~ 글자 길이 절반까지 묶어서 보는 경우를 모두 확인한다
for i in range(1, int(len(s)/2)+1):
    temp = make_word(s,i)
    words.append((temp, len(temp)))

# 경계값 에러를 항상 생각하자
if len(s) == 1:
    print(1)
# word에는 모든 경우의 압축문장과 크기가 들어있으므로 정렬 필요
else:
    words = sorted(words, key=lambda x:x[1])
    print(words[0][1])