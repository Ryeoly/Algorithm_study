s = input()
count = dict()
count["0"] = 0
count["1"] = 0

if len(s) == 0:
    print(0)

pre_char = s[0]
count[s[0]] = 1

for i in range(1, len(s)):
    if s[i] != pre_char:
        count[s[i]] += 1
        pre_char = s[i]

print( min(count["0"], count["1"], 1 + count["0"], 1 + count["1"]) )
