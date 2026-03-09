
while True:
    su = 0
    a = int(input())
    if a==0:
        break
    else:
        for i in range(5):
            if a%2==0:
                su += 2*i+a
            else:
                su += 2*i+a+1
    print(su)

