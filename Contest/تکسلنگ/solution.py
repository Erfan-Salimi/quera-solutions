n1 = input()
n2 = input()
n3 = input()
f = 5
l = len(n1)

for i in range(int(l/5)):
    if n1[f - 5 : f] == "*****":
        print(end="T")
    elif n2[f - 5 : f] == "o***o":
        print(end="A")
    elif n1[f - 5 : f] == "**o**":
        print(end="M")
    elif n1[f - 5 : f] == "*ooo*" and n2[f - 5 : f] == "*o*o*":
        print(end="N")
    elif n1[f - 5 : f] == "*ooo*" and n3[f - 5 : f] == "*ooo*" and n2[f - 5 : f] == "oo*oo":
        print(end="X")
    f += 5
