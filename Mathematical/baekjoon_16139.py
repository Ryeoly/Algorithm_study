import sys

sentence = list(map(str, sys.stdin.readline().rstrip()))
q = int(sys.stdin.readline())
alphas = set(sentence)
dic = dict()

for alpha in alphas:
    dic[alpha] = [0]*200001

if len(sentence) != 0:
    dic[sentence[0]][0] = 1

for i in range(1, len(sentence)):
    for alpha in alphas:
        if sentence[i] != alpha:
            dic[alpha][i] = dic[alpha][i-1]
        else:
            dic[alpha][i] = dic[alpha][i-1]+1


for i in range(q):
    a, l, r = sys.stdin.readline().split()
    if a in alphas:
        if int(l) == 0:
            print(dic[a][int(r)])
        else:
            print(dic[a][int(r)] - dic[a][int(l)-1])

    else:
        print(0)