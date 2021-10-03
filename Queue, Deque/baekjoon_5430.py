import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    p = list(map(str, sys.stdin.readline().rstrip()))
    n = int(sys.stdin.readline())
    numbers = sys.stdin.readline().rstrip()
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(str, numbers[1:len(numbers) - 1].split(",")))
    check = True
    evidence = 0
    for j in p:
        if j == "R":
            check = not check
        elif j == "D":
            if check:
                try:
                    arr.popleft()
                except:
                    arr.clear()
                    evidence = 1
                    break
            elif check is False:
                try:
                    arr.pop()
                except:
                    arr.clear()
                    evidence = 1
                    break
        else:
            print("is not R, D")
    if evidence == 1:
        print("error")
    else:
        if check is False:
            arr.reverse()
        print("[" + ",".join(arr) + "]")


# 간단하다고 생각했는데 그렇지 않았던 문제
# 우선 시간 제한으로 인해 deque.reverse()를 못쓴다는 것을 인지하는데까지 오래걸림
# reverse를 하는 목적은 결국 빼주는 위치를 결정하는 것이기 때문에 앞, 뒤만 체크해주면된다.(R의 홀짝을 체크해주면된다)
# 마지막에 출력할 때 reverse를 시키고 출력해야되는지 판단을 꼭해야한다.
# 코딩을 잘하는 사람들은 D의 개수를 count해서 더 빠지면 error를, 삭제를 미리해준다.
# 마지막 출력 포멧도 기억하자!