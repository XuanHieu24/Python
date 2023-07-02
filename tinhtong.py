from math import*
n = int(input("N = "))
a = 0
s = 0
for i in range(0,n+1):
    a+=i
    s+=sqrt(a)
print("F(",n,") = ",round(s,7),sep = "")
