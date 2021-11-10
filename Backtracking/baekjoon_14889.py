import sys

n = int(sys.stdin.readline())
s = list()

for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

a_team = []
result = []
INF = int(1e9)

def dfs(start):
    if len(a_team) == int(n / 2):
        value = team_value(a_team)
        global INF
        if value <= INF:
            INF = value
            return

    for i in range(start, n):
        if i not in a_team:
            a_team.append(i)
            dfs(i+1)
            a_team.pop()

def team_value(a_team):
    b_team = list(range(n))
    for i in a_team:
        b_team.remove(i)

    o_sum = 0
    t_sum = 0

    for i in a_team:
        for j in a_team:
            o_sum += s[i][j]

    for i in b_team:
        for j in b_team:
            t_sum += s[i][j]

    return abs(o_sum - t_sum)

dfs(0)
print(INF)

# 1. 모든 경우의 수를 다 확인할 경우 시간이 되는가
# 2. 시간은 넉넉했기에 모든 조합을 구하는 방법을 고안.
# 2. combination을 이용해 구할 수 있지만, 직접 구해 보는 법을 선택
# 3. 최소 값을 INF에 저장시켜 출력한다.