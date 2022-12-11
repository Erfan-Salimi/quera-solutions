n = input()
new_str = []
s = 0

for i in n:
    if i == "=" and s != 0:
        del new_str[-1]
        s -= 1
    elif i != "=":
        new_str.append(i)
        s += 1

print("".join(new_str))
