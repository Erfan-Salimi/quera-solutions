n = (int(input())*2)+1
m = []

if n == 1:
    print("*")
else:
    for i in range(1, n+1, 2):
        space = int((n - i) / 2)

        print(space*" "+i*"*")
        if i != n:
            m.append(space*" "+i*"*")
    
    m = m[::-1]
    for i in range(len(m)):
        print(m[i])
