even = []
od = []
for i in range(15):
    a = int(input())
    if a % 2 == 0:
        even.append(a)
        if len(even) == 5:
            for index in range(len(even)):
                print(f"par[{index}] = {even[index]}")


    else:
        od.append(a)
        if len(od) == 5:
            for index,value in enumerate(od):
                print(f"impar[{index}] = {value}")

evenn = even[5:]
odd = od[5:]
for o in range(len(odd)):
    print(f"impar[{o}] = {odd[o]}")
for h in range(len(evenn)):
    print(f"par[{h}] = {evenn[h]}")


