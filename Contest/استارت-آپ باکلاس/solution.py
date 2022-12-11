n = [int(i) for i in input().split(" ")]
tedad = [0 for i in range(4)]
i = 0

while True:
    if 0 in n:
        break
    else:
        n[0] -= 1
        n.insert(0, n[-1])
        n.pop()
        n.insert(0, n[-1])
        n.pop()
        if i == len(n):
            i = 0
        tedad[i] += 1
        i += 1

tedad = [str(i) for i in tedad]
print(" ".join(tedad))
