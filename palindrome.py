text = input("Soz ve ya cümle yazin: ")

cleaned = text.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print("beli")
else:
    print("xeyr")