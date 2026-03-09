li = list(map(int,input().split()))
all = 0
a = li[0]
b = li[-1]

for i in range(a, a+b):
    all += i
print(all)
