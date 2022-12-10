ali1 = int(input())
ali2 = int(input())

torob1 = int(input())
torob2 = int(input())

if ali2 == torob2:
    print("WAIT WAIT")
elif torob1 > ali1:
    if ali2 > torob2:
        print("SEE YOU")
    else:
        print("BORO BORO")
else:
    if ali2 < torob2:
        print("SEE YOU")
    else:
        print("BORO BORO")
