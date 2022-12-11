n = input()

while len(n) != 0 and n[0] == "0":
    n = n[1:]

if n == "":
    print(0)
else:
    print(n)
