import sys

stack = list()
evidence = 0
while 1:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break

    for i in line:
        if i == ".":
            if len(stack) == 0 and evidence == 0:
                print("yes")
            else:
                print("no")
            stack.clear()
            evidence = 0
        if i == "(" or i == "[":
            stack.append(i)
        elif (i == ")" or i == "]") and len(stack) == 0:
            evidence = 1
        elif i == ")" and stack[len(stack)-1] == "(":
            stack.pop()
        elif i == "]" and stack[len(stack)-1] == "[":
            stack.pop()
        elif i == ")" or i == "]":
            evidence = 1