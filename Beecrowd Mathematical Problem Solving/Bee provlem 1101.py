##
while True:
    a, b = map(int,input().split())
    A = min(a, b)
    B = max(a, b)
    if a<=0 or b<=0:
        break
    else:
        l = []
        for i in range(A,B+1):
            l.append(i)
            r = " ".join(map(str, l))

        print(f"{r} Sum={sum(l)}")
