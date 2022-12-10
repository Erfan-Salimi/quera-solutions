n, m = [int(i) for i in input().split(' ')]
dict_ = {}

for i in range(n):
    a = input().split()
    dict_[a[0]] = a[1]

r = []
j = 0
q = input().split()

for i in q:
    if j < m:
        if i in dict_.keys():
            r.append(dict_[i])
    r.append("kachal!")

print(*r)
