plate = input("Avtomobil nömresini yazin: ")

if len(plate) != 9:
    print("Yanlis format")
elif plate[2] != "-" or plate[5] != "-":
    print("Yanlis format")
elif not plate[0:2].isdigit():
    print("Yanlis format")
elif not (plate[3:5].isalpha() and plate[3:5].isupper()):
    print("Yanlis format")
elif not plate[6:9].isdigit():
    print("Yanlis format")
else:
    print("Duzgun format")