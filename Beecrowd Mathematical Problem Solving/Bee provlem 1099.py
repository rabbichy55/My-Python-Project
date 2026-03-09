##
for i in range(int(input())):
    a, b = input().split()
    a, b = int(a), int(b)
    if a >= b:
        l = []
        for i in range(b+1, a):

            if i%2 != 0:
                l.append(i)
        print(sum(l))
    else:
        l = []
        for i in range(a+1, b):
            if i%2 != 0:
                l.append(i)
        print(sum(l))

##
for i in range(int(input())):
    a, b = map(int, input().split())
    a = min(a, b)
    b = max(a,b)

    l = []
    for i in range(a+1, b):
        if i%2 != 0:
            l.append(i)
    print(sum(l))
