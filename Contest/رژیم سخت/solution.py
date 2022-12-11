n = input()
g = 0
r = 0
y = 0

for i in n:
    if i == "G":
        g += 1
    elif i == "R":
        r += 1
    elif i == "Y":
        y += 1

if r + y == 5 or r >= 3 or (r >= 2 and y >= 2):
    print("nakhor lite")
else:
    print("rahat baash")
