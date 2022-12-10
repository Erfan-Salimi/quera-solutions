n = input().split()
m = []
s = 0

for i in range(int(n[0])):
    m.append(input().split())

for i in m:
    for j in range(len(i)):
        i[j] = int(i[j])

for i in range(int(n[0])):
    for j in range(int(n[1])):
        if i != 0 and i != int(n[0])-1 and j != 0 and j != int(n[1])-1:
            if m[i][j-1] > m[i][j] and m[i][j+1] > m[i][j] and m[i-1][j] < m[i][j]  and m[i+1][j] < m[i][j]:
                d = True
                
            elif m[i][j-1] < m[i][j] and m[i][j+1] < m[i][j] and m[i-1][j] > m[i][j]  and m[i+1][j] > m[i][j]:
                d = True

            else:
                d = False
            if d == True:
                s += 1

print(s)
