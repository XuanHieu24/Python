n = int(input("Nhap N duong: "))
gt = 1
s = 1
for i in range(2,n+1):
    gt*=i
    s+=gt
print("F(",n,") = ",s,sep)
