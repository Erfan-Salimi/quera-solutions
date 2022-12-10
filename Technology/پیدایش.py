def find(n1, n2, n3):
    m = [1, 2, 3, 4]
    n = [n1, n2, n3]
    l = []

    for i in m:
        if i not in n:
            return i
