n = int(input())

if n%5 == 0:
    print(int(n/5))
elif (n%5)%3 == 0:
    print(int(n//5)+int((n%5)/3))
else:
    count = 1
    evidence = 0
    for i in range(int(n//3)+1):
        if (n-count*3)%5 == 0:
            print(count+int((n-count*3)/5))
            evidence += 1
            break
        count += 1
    if evidence == 0:
        if n%3 == 0:
            print(int(n/3))
        else:
            print(-1)