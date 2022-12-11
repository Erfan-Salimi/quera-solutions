n = input().split()
m = input().split()
s = 0
b = 0

for i in range(len(m)):
    m[i] = int(m[i])
    if m[i] == int(n[1]):
        b += 1
    else:
        s += m[i]

b += s / int(n[1])

if b == int(b):
    print(int(int(n[0]) - b))
else:
    print(int(n[0]) - (int(b)+1))
