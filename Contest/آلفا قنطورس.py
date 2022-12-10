a, b = [int(i) for i in input().split()]
alpha = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
r = []

while True:
    r.append(str(alpha[a%b]))
    a //= b
    if a == 0: break

print(''.join(r[::-1]))
