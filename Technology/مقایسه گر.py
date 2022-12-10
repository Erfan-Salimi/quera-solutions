def compare(string1, string2):
    S1 = [i for i in string1]
    S2 = [i for i in string2]

    while True:
        try:
            if ord(S1[0]) < ord(S2[0]):
                del S1[0]
                S1 = S1[::-1]
                S2 = S2[::-1]
            elif ord(S1[0]) > ord(S2[0]):
                del S2[0]
                S2 = S2[::-1]
                S1 = S1[::-1]
            elif ord(S1[0]) == ord(S2[0]):
                del S1[0]
                del S2[0]
                S2 = S2[::-1]
                S1 = S1[::-1]
        except:
            break

    if len(S1) == 0 and len(S2) != 0:
        S2 = S2[::-1]
        return("".join(S2)) 

    elif len(S2) == 0 and len(S1) != 0:
        S1 = S1[::-1]
        return("".join(S1))
        
    else:
        return("Both strings are empty!")
