n = int(input())
cards = [0] + list(map(int, input().split()))
value = [0] * (n+1)

value[1] = cards[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if value[i] < value[i-j] + cards[j]:
            value[i] = value[i-j] + cards[j]

print(value[-1])