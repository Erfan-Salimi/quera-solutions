s = "codecup6"
n = int(input())

while n > len(s):
    s += s

print(s[n-1])