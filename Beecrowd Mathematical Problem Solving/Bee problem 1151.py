f = 0
b = 1
a = int(input())

if 0<a<46:

    for i in range(a):
        if i+1 != a:
            print(f, end=" ")
        else:
            print(f, end='')

        c = f+b
        f = b
        b = c


n = int(input())

li = [0, 1]
to = 0

for i in range(n-2):
    to = li[-1] + li[-2]
    li.append(to)
print(' '.join(map(str,li)))