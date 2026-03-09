age = 0
len = 0

while True:
    a = int(input())

    if a <0:
        break
    else:
        age += a
        len += 1

avg = age/len
print(f"{avg:.2f}")