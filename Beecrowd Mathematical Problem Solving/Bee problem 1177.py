a = int(input())
sequence = []

for i in range(1000):
    sequence.append(i%a)


for idx, value in enumerate(sequence):
    print(f"N[{idx}] = {value}")

# for j in range(len(sequence)):
#     print(j, sequence[j])