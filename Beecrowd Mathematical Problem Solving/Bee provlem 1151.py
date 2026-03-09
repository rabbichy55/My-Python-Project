li = []


while True:
    a = int(input())
    li.append(a)
    if a>li[0]:
        second = a
        break

first = li[0]
total = 0
count = 0

for i in range(first, second+1):
    if total<second:
        total += i
        count += 1

print(count)