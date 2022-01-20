# 브루트 포스트란 모든값을 대입한다는 개념

n = int(input())

answer = 0
count = 0

while 1:
    if '666' in str(answer):
        count += 1
    if count == n:
        print(answer)
        break
    answer += 1