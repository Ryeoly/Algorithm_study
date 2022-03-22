import itertools
L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
mo = ['a', 'e', 'i', 'o', 'u']

combinations = list(itertools.combinations(arr, L))

for combination in combinations:
    c_mo = 0
    c_ja = 0
    for char in combination:
        if char in mo:
            c_mo += 1
        else:
            c_ja += 1
    if c_mo >= 1 and c_ja >= 2:
        print("".join(combination))

