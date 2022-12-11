n = input()
p = 0

for i in n:
    if i == "L" or i == "F" or i == "T" or i == "D":
        p += 1

print(2**p)
