li = []
ti = []
for i in range(20):
    a = int(input())
    li.append(a)
    ti.append(i)

li.reverse()
for j, e in zip(li, ti):
    print(f"N[{e}] = {j}")

##
li = []
for i in range(20):
    a = int(input())
    li.append(a)

count = 0
for j in li[::-1]:  # list slicing from negative
    print(f"N[{count}] = {j}")
    count += 1
