n, m1, m2 = input().split()
n, m1, m2 = int(n), int(m1), int(m2)
ln, lm = list(range(0, n-1, m1)), list(range(0, n-1, m2))
l = list(dict.fromkeys(ln+lm))
print(len(l))