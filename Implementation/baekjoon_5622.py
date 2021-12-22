two = ['A', 'B', 'C']
three = ['D', 'E', 'F']
four = ['G', 'H', 'I']
five = ['J', 'K', 'L']
six = ['M', 'N', 'O']
seven = ['P', 'Q', 'R', 'S']
eight = ['T', 'U', 'V']
nine = ['W', 'X', 'Y', 'Z']

arr = list(map(str, input()))
answer = 0
for i in arr:
    if i in two:
        answer += 3
    elif i in three:
        answer += 4
    elif i in four:
        answer += 5
    elif i in five:
        answer += 6
    elif i in six:
        answer += 7
    elif i in seven:
        answer += 8
    elif i in eight:
        answer += 9
    elif i in nine:
        answer += 10

print(answer)