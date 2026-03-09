for i in range(int(input())):
    count = 0
    pa, pb, g1, g2 = (input().split())
    int(pa), int(pb)
    PA, PB = int(pa), int(pb)
    G1, G2 = float(g1), float(g2)

    while PA <= PB:
        PA += int(PA*(G1/100))
        PB += int(PB*(G2/100))
        count += 1

        if count > 100:
            break


    if count > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{count:.0f} anos.")
#1172