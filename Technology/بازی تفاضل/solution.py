def game(n):
    n = str(n)
    n1 = int(n[0])
    n2 = int(n[1])

    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1
