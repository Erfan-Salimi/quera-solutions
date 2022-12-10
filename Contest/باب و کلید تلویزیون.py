n = input().split()

tedad = int(n[0])
shabake = int(n[1])
feshar = int(n[2])
shabake_ha = []

for i in range(tedad):
    shabake_ha.append(input())

for i in range(1, feshar+1):
    if shabake == tedad:
        shabake = 0
    shabake += 1

print(shabake_ha[shabake - 1])
