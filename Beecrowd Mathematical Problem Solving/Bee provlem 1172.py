#1172
li = []
for i in range(10):
    a = int(input())
    li.append(a)
    if li[i] <= 0:
        li[i] = 1
    print(f"X[{i}] = {li[i]}"