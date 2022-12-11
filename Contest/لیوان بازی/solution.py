n, m = input().split()
dict_ = {"L": 0, "M": 1, "R": 2}
l = [0, 0, 0]
l[dict_[m]] = 1

for i in range(int(n)):
    a, b = [i for i in input().split()]
    l[dict_[a]], l[dict_[b]] = l[dict_[b]], l[dict_[a]]

j = 0
for i in l:
    if i != 0:
        print(list(dict_.keys())[j])
        break
    j += 1
