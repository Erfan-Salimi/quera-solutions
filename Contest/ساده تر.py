n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

Sum = n1 + n2 + n3 + n4
Average = Sum / 4
Product = n1 * n2 * n3 * n4
MAX = max(n1, n2, n3, n4)
MIN = min(n1, n2, n3, n4)

print(f"Sum : {'%.6f' % Sum}\nAverage : {'%.6f' % Average}\nProduct : {'%.6f' % Product}\nMAX : {'%.6f' % MAX}\nMIN : {'%.6f' % MIN}")
