n = list(map(int, input()))

front = n[:int(len(n)/2)]
end = n[int(len(n)/2):]

if sum(front) == sum(end):
    print("LUCKY")
else:
    print("READY")