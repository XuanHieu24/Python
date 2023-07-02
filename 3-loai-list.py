n=int(input("Nhap N: "))
A = []
B = []
C = []
for i in range (1,n+1):
    d=input("Nhap gia tri thu "+str(i)+": ")
    try:
        A.append(int(d))
    except:
        try:
            B.append(float(d))
        except:
            C.append(d)
print("A =",sorted(A, reverse=True))
print("B =",sorted(B, reverse=True))
print("C =",sorted(C, reverse=True))
