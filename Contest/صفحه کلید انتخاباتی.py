n = int(input())
p = 0
s = ""

for i in range(n):
    o = input()
    
    if o =="CAPS":
        p += 1
        p = p%2
    else:
        if p==0:
            s += o.lower()
        if p==1:
            s += o.upper()

print(s)
