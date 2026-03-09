# beecrowd | 1094.
list_1 = []
list_2 = []
list_3 = []
for i in range(int(input())):
    a = list(map(str,input().split()))
    if "C" in a:
        list_1.append(a)
    elif "R" in a:
        list_2.append(a)
    elif "S" in a:
        list_3.append(a)

# convert 2D  list to 1D
flat_list_1 = sum(list_1, [])
int_flat_1 = []
# convert list int
for item in flat_list_1:
    if item.isdigit():  # check if it's a number
        int_flat_1.append(int(item))
    else:
        int_flat_1.append(item)

flat_list_2 = [int(item) if item.isdigit() else item for item in sum(list_2, [])]
flat_list_3 = [int(item) if item.isdigit() else item for item in sum(list_3, [])]

# Total sum of all list
total_sum = 0

for i in int_flat_1 + flat_list_2 + flat_list_3:
    if isinstance(i, int):  # check if it's a number
        total_sum += i  # Add to sum

print(f"Total: {total_sum} cobaias")

# specific sum of every list number
num_1 = 0
for i in int_flat_1:
    if isinstance(i, int):
        num_1 += i
print(f"Total de coelhos: {num_1}")

#
num_2 = 0
for i in flat_list_2:
    if isinstance(i, int):
        num_2 += i
print(f"Total de ratos: {num_2}")

#
num_3 = 0
for i in flat_list_3:
    if isinstance(i, int):
        num_3 += i
print(f"Total de sapos: {num_3}")


print(f'''Percentual de coelhos: {(num_1/total_sum)*100:.2f} %
Percentual de ratos: {(num_2/total_sum)*100:.2f} %
Percentual de sapos: {(num_3/total_sum)*100:.2f} %''')



My second way:

l1 = []
l2 = []
l3 = []

for i in range(int(input())):
    a = list(map(str, input().split()))
    if "C" in a:
        l1.append(a)
        l11 = sum(l1, [])
        l111 = []
        for i in l11:
            if i.isdigit():
                l111.append(int(i))
    elif "R" in a:
        l2.append(a)
        l22 = sum(l2, [])
        l222 = []
        for i in l22:
            if i.isdigit():
                l222.append(int(i))
    else:
        l3.append(a)
        l33 = sum(l3, [])
        l333 = []
        for i in l33:
            if i.isdigit():
                l333.append(int(i))

total_sum = sum(l111) + sum(l222) + sum(l333)
print(total_sum)

l1111 = sum(l111)
l2222 = sum(l222)
l3333 = sum(l333)
print(f"({l1111} {l1111/total_sum*100:.2f}), {l2222}, {l3333}")



Another way:

rabbit = []
rat = []
frog = []

for i in range(int(input())):
    amount, type = input().split()
    amount = int(amount)

    if 1<= amount <= 15:

        if type == "C":
            rabbit.append(amount)

        if type == "R":
            rat.append(amount)

        if type == "S":
            frog.append(amount)

t_rabbit = sum(rabbit)
t_rat = sum(rat)
t_frog = sum(frog)

print(t_rabbit)
print(t_rat)
print(t_frog)


