a = int(input())
n = int(input())
v = input()
m = []

for i in v:
    m.append(i)

for i in range(n):
    last = m[-1]
    del m[-1]
    m.insert(0, last)
    
    for i in range(len(m)):
        if m[i] == 'z':
            m[i] = 'a'
        else:
            m[i] = chr(ord(m[i])+1)

print(''.join(m))