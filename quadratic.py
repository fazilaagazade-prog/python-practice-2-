a = float(input("a yazin: "))
b = float(input("b yazin: "))
c = float(input("c yazin: "))

if a == 0:
    print("Bu kvadrat tenlik deyil")
else:
    D = b ** 2 - 4 * a * c
    print("Diskriminant:", D)

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print("İki kok var:", x1, "və", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("Bir kok var:", x)
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print("Kompleks kokler:", x1, "və", x2)