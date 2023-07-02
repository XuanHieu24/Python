def giaithua(n):
    giaithua = 1
    if ( n == 0 or n == 1):
        return 1
    else:
        for i in range(2, n+1):
            giaithua = giaithua*i
        return giaithua
n = int(input("N = "))
print("Giai thua cua", n ,"là", giaithua(n))
