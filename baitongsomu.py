n = int(input("N = "))
s =2**n
t=0
while s>0:
    t =t+s%10
    s//=10
print("Tong =",t)
