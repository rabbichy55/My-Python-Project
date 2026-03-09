matches = 0
w = 0  # Inter wins
r = 0  # Gremio wins
d = 0  # Draws

while True:
    # Read scores for Inter and Gremio
    a, b = map(int, input().split())
    matches += 1  # Increment match count

    # Update win/draw counts
    if a > b:
        w += 1
    elif b > a:
        r += 1
    else:
        d += 1

    # Ask the user if they want to continue
    print("Novo grenal (1-sim 2-nao)")
    e = int(input())

    if e == 1:
        continue  # Restart the loop for a new match
    elif e == 2:
        # Print results and exit
        print(f"{matches} grenais")
        print(f"Inter:{w}\nGremio:{r}\nEmpates:{d}")
        if w > r:
            print("Inter venceu mais")
        elif r > w:
            print("Gremio venceu mais")
        else:
            print("Não houve vencedor")
        break  # Exit the loop
    else:
        print("Invalid input. Please enter 1 or 2.")