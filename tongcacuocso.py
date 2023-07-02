n = int(input("N = "))
s = 0
for i in range(1,n+1):
    if n % i == 0:
        s = s + i
print("Tong cac uoc cua "+str(n)+" la",s)
