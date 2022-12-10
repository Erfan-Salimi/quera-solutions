ls = [input() for i in range(5)]
s = []

for i in range(len(ls)):
    if "FBI" in ls[i]:
        s.append(str(i+1))

if len(s) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(s))
