n=int(input("N = "))
a, b=0,1
while b!=n:
    if b>n:
        break
    a,b=b ,a+b
print("N la so fibonacci chan" if b==n and (n%2)==0 else "N khong phai la so fibonacci chan")
