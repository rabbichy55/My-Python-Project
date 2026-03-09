N = int(input())
mode = input()

matrix = []

for i in range(12):
    row = []
    for items in range(12):
        items_rows = float(input())
        row.append(items_rows)

    matrix.append(row)

if mode == "S":
    output = sum(matrix[N])
    print(f"{output:.1f}")
if mode == "M":
    output = sum(matrix[N])/12
    print(f"{output:.1f}") 