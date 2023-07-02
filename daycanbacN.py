n=int(input("N = "))
s=0
a=0
for i in range(1,n+1):
    a=a+i
    s=s+pow(a,1/i)
print("F(",n,") = %.7f"%s,sep="")
