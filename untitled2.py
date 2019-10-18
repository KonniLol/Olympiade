n = int(input("Enter Number:"))
s = int(input("Enter start power:"))
e = int(input("Enter end power:"))

for i in range(s,e+1,1):
    print(n**i,end=';')