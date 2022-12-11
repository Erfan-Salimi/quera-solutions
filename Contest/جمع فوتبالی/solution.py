for i in range (int(input())):
    result = [int(j) for j in input().split()] 
    if result[0] + result[2] > result[1] + result[3]:
        print("perspolis")
    elif result[0] + result[2] < result[1] + result[3]:
        print("esteghlal")
    else:
        if result[1] > result[2]:
            print("esteghlal")
        elif result[1] < result[2]:
            print("perspolis")
        else:
            print("penalty")
