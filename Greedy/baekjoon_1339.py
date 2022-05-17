import sys

n = int(sys.stdin.readline())
arr = []
temp = ["0","1","2","3","4","5","6","7","8","9"]
dic = dict()
result_dic = dict()
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())

for i in arr:
    for j in range(len(i)-1, -1, -1):
        if i[j] in dic:
            dic[i[j]] += 10**(len(i)-j)
        else:
            dic[i[j]] = 10**(len(i)-j)

sort_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

for item in sort_dic:
    result_dic[item[0]] = temp.pop()
result = 0
for i in arr:
    t = ""
    for j in i:
        t = t+result_dic[j]
    result += int(t)

print(result)