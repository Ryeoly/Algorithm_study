# my solve
arr = list(input())
temp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number = []
string = []
for i in arr:
    if i in temp:
        number.append(int(i))
    else:
        string.append(i)

string.sort()
if len(number) > 0:
    print("".join(string)+str(sum(number)))
else:
    print("".join(string))

# # codingtest solve
# data = input()
# result = []
# value = 0
#
# for x in data:
#     if x.isalpha():
#         result.append(x)
#     else:
#         value += int(x)
#
# result.sort()
# if value !=0:
#     result.append(str(value))
#
# print("".join(result))
#
# #