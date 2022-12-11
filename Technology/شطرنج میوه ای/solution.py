def fruits(tuple_of_fruits):
    m = []

    for i in tuple_of_fruits:
        name = i["name"]
        shape = i["shape"]
        mass = i["mass"]
        volume = i["volume"]

        if shape == 'sphere' and 300 <= mass <= 600 and 100 <= volume <= 500:
            m.append(name)

    s = {}
    for i in m:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    return s
