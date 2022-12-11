def print_pascal(n):
    for line in range(0, n): 
        for i in range(0, line + 1): 
            print(binomial_coeff(line, i), 
                " ", end = "") 
        print() 


def binomial_coeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
      
    return res 


n = int(input())
print_pascal(n) 
