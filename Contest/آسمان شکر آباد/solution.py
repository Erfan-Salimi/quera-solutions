n = input()
n = n.split()
ns = []
r = 0

for i in range(int(n[0])):
    ns.append(input())

for i in ns:
    for t in i:
        if t == "*":
            r += 1

print(r)
