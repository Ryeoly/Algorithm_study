import sys

n = int(sys.stdin.readline())
score = list()
for i in range(n):
    score.append(int(sys.stdin.readline()))

if n == 1:
    print(score[0])
elif n == 2:
    print(score[0]+score[1])
else:
    dp = [0] * (n)
    dp[0] = score[0]
    dp[1] = max(score[1], score[0]+score[1])
    dp[2] = max(score[0]+score[2], score[1]+score[2])
    for i in range(3, n):
        dp[i] = max(score[i]+score[i-1]+dp[i-3], score[i]+dp[i-2])
    print(dp[n-1])


# 중요 포인트는 0,1,2번째를 제외한 부분에서 비교하는 값들
# 무조건 자기 위치는 밟는 경우만을 비교한다.