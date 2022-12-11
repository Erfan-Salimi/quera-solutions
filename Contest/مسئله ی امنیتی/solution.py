n = input()
m = []

for i in n:
    m.append(i)

for i in range(len(m)):
    X = 0
    if 97 <= ord(m[i]) <= 122:
        up = False
        A = ord(m[i])-97
    else:
        up = True
        A = ord(m[i])-65

    m[i] = m[i].lower()
    for j in range(len(m)):
        s = m[j].lower()
        if s == m[i]:
            X += 1

    y = (X * A +1) % 26
    if up == True:
        print(end=f"{chr(y+65)}")
    else:
        print(end=f"{chr(y+97)}")
