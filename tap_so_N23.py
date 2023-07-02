N = int(input("N = "))
a = [1]
clength = 1
i2 = 0
i3 = 0

while clength < N:
    N2 = a[i2]*2 + 1
    N3 = a[i3]*3 + 1

    if N2 < N3:
        a.append(N2)
        i2 += 1
    elif N2 > N3:
        a.append(N3)
        i3 += 1
    else:
        a.append(N2)
        i2 += 1
        i3 += 1
        clength += 1

print(N, "So dau tien cua N23:", end = " ")
print(*a)
