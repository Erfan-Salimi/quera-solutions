def separator(ls):
    fard = []
    zoj = []

    for i in ls:
        if i % 2 == 0 or i == 0:
            zoj.append(i)
        else:
            fard.append(i)
    
    return zoj, fard
