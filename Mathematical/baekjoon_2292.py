k = int(input())
n=2
if k == 1:
    print(1)
else:
    while 1:
        if ((n-1)*(3*(n-2)))+1 < k <= (n*(3*(n-1)))+1:
            print(n)
            break
        n += 1