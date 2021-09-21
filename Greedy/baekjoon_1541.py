def point(str):
    number = ""
    add = 0
    for i in range(len(str)):
        if str[i] != "-" and str[i] != "+":
            number = number + str[i]
        elif str[i] == "+":
            add += int(number)
            number = ""
        elif str[i] == "-":
            add += int(number)
            number = ""
            return i+1,add
    add += int(number)
    print(add)
    return "end","end"

str = input()
i, add = point(str)
if i == "end":
    exit()
number = ""
sub = 0
for j in str[i:]:
    if j != "-" and j != "+":
        number = number + j
    else:
        sub += int(number)
        number = ""
sub += int(number)
print(add-sub)