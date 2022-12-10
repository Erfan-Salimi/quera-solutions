n = input().split()
t, a, b = int(n[0]), int(n[1]), int(n[2])

kol = 0
ar = 0
ma = 0

while True:
    ar += 1
    kol += 1
    kol += a

    if kol >= t:
        break
    
    ma += 1
    kol += 1
    kol += b

    if kol >= t:
        break

print(f'{ar} {ma}')
