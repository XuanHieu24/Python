from math import*
n = int(input("N = "))
if n%2 == 0:
        s=0
        for i in range(2,n+1,2):
                s+=i**2
print("P(",n,") = ",s,sep="")   
