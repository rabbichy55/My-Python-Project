n = int(input())
a = 1

if 0<n<13:
    for i in range(1, n+1):
        a *= i

print(a)