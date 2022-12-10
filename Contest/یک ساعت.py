n = input().split()

m = 12 - int(n[0])
if m == 12:
    m = 0

b = 60 - int(n[1])
if b == 60:
    b = 0

if len(str(m)) == 1 and len(str(b)) == 1:
    print(f"0{m}:0{b}")
elif len(str(b)) == 1:
    print(f"{m}:0{b}")
elif len(str(m)) == 1:
    print(f"0{m}:{b}")
else:
    print(f"{m}:{b}")
