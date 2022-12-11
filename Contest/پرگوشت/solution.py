n = input()
n = n.split()

number = []
numbers = []
goosht = 0
goosht2 = 0

n1 = int(n[0])
n2 = int(n[1])

for i in range(n1):
    numbers.append(input())

for k in numbers:
    for l in k:
        if l == "*":
            goosht += 1

for i in range(n1):
    number.append(input())

for k in number:
    for l in k:
        if l == "*":
            goosht2 += 1

print(f"{goosht} {goosht2}")