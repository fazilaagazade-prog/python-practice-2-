number = input("Nömreni yazin: ")

number = number.replace("-", "").replace(" ", "")

if len(number) != 10:
    print("Yanliş nömrə")
else:
    prefix = number[:3]

if prefix in ("050", "051", "010"):
        print("Azercell")
elif prefix in ("055", "099"):
        print("Bakcell")
elif prefix in ("070", "077"):
        print("Nar")
else:
        print("Namelum operator")