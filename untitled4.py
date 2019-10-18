ln = [2,4,6,8,10]
lm = [3,6,9]
l = ln + lm
print(l)
l = list(dict.fromkeys(l))
print(l)
print(len(l))