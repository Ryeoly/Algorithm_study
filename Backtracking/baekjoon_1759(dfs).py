L, C = map(int, input().split())

def dfs(start, dep):
    if dep == L:
        count = 0
        for i in answer:
            if i in mo:
                count += 1
        if L-count >= 2 and count >= 1:
            print("".join(answer))

    for i in range(start, C):
        answer.append(arr[i])
        dfs(i+1, dep+1)
        answer.pop()

arr = list(map(str, input().split()))
arr.sort()
mo = ['a', 'e', 'i', 'o', 'u']

answer = list()
dfs(0, 0)
