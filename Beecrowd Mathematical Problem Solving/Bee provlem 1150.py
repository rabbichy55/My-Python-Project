li = []  # declare a list

while True:
    a = int(input())
    li.append(a)
    first = li[0]

    if a>first:
        second = a
        break

total = 0
count = 0
for i in range(first, second+1):
    if total<second:
        total += i
        count += 1

print(count)
