def add(s):
    t = "!"
    n = len(s)
    if (s.count(t,n-3) == 3): s = s
    elif (s.count(t,n-2) == 2): s = s+t
    elif (s.count(t,n-1) == 1): s = s+t*2
    elif (s.count(t,n-1) == 0): s = s+t*3
    return s
s = input("Nhap chuoi: ")
print("Chuoi S sau khi bo sung them dau cham than: '",add(s),"'",sep = "")
