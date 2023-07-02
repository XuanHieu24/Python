a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
if a==b==c:
    print("Xep tang dan:",a)
elif a==b and c>a:
    print("Xep tang dan:",a,c)
elif a==c and b>c:
    print("Xep tang dan:",a,b)
elif b==c and a>c:
    print("xep tang dan:",b,a)
elif b==c and a<b:
    print("Xep tang dan:",a,b)
elif a>b>c:
    print("xep tang dan:",c,b,a)
elif a>c>b:
    print("Xep tang dan:",b,c,a)
elif b>a>c:
    print("Xep tang dan:",c,a,b)
elif b>c>a:
    print("Xep tang dan:",a,c,b)
elif c>a>b:
    print("Xep tang dan:",b,a,c)
elif c>b>a:
    print("Xep tang dan:",a,b,c)
