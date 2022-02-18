import sys
import itertools

def check(student, teacher, wall):
    for i in teacher: # 선생 한명씩 골라서 시야에 학생이 있는지 확인하기 위함
        t_col, t_row = i[0], i[1]

        for j in student: # 모든 학생들이 시야에 있는지 확인하기 위함
            s_col, s_row = j[0], j[1]

            if s_col == t_col or s_row == t_row: # 시야에 학생이 있는 경우
                evidence = False
                for q in wall: # 학생과 선생 사이에 벽이 있는지 확인
                    w_col, w_row = q[0], q[1]
                    if s_col == w_col == t_col and (t_row < w_row < s_row or s_row < w_row < t_row): # 사이에 벽이 있는 경우
                        evidence = True
                    elif s_row == w_row == t_row and (t_col < w_col < s_col or s_col < w_col < t_col):
                        evidence = True
                if not evidence:
                    return False

    return True

n = int(sys.stdin.readline())
arr = list()
for i in range(n):
    arr.append(list(sys.stdin.readline().split()))

student = list()
teacher = list()
empty = list()
for i in range(n):
    for j in range(n):
        if arr[i][j] == "S":
            student.append((i, j))
        elif arr[i][j] == "T":
            teacher.append((i, j))
        else:
            empty.append((i, j))

walls = list(itertools.combinations(empty, 3))

result = "NO"
for wall in walls:
    if check(student, teacher, wall):
        result = "YES"
        break
print(result)
