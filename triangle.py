year = int(input("İl yazin: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("uzun il")
else:
    print("uzun deyil")