n = int(input())
line = 1
while 1:
    if (line-1)*line < 2*n <= (line+1)*line:
        break
    line += 1

ran = int((line-1)*line/2)+1
if line%2 == 0:
    print("{0}/{1}".format(1+n-ran, line-n+ran))
else:
    print("{0}/{1}".format(line-n+ran, 1+n-ran))