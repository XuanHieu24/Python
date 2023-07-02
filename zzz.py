n = int(input("N = "))
a = 0
f = 0
for i in range(0,n+1):
    a+=i
    f+=a**0.5
print("F(",n,") = ","%.7f" % f,sep = "")
