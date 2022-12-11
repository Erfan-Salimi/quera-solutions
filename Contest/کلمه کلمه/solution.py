n = input()
s = 0

for i in range(len(n)):
    if n[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',]:
        s += 1

print(2**s)
