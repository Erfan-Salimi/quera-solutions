from collections import Counter

n = int(input())
a = dict(Counter([int(i) for i in input().split()]))
ls = []

for key, value in a.items():
    if value == 1:
        ls.append(key)

s = 0
for i in ls:
    s = s ^ i

print(s)