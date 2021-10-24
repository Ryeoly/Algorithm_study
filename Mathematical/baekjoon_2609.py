n, m = map(int, input().split())

def factor(number):
    arr = list()
    for i in range(1, number+1):
        if number%i == 0:
            arr.append(i)
    return arr

def multiple(number, max):
    arr = list()
    for i in range(1, max+1):
        arr.append(i*number)
    return arr

n_factor = factor(n)
m_factor = factor(m)


for i in n_factor[::-1]:
    if i in m_factor:
        print(i)
        break

n_multiple = multiple(n, m)
m_multiple = multiple(m, n)

if n >= m:
    for i in m_multiple:
        if i in n_multiple:
            print(i)
            break
else:
    for i in n_multiple:
        if i in m_multiple:
            print(i)
            break