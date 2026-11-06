day = int(input("Gün yazin: "))
month = int(input("Ay yazin: "))
year = int(input("İl yazin: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if month < 1 or month > 12:
    print("yoxdur")
else:
    if month in (4, 6, 9, 11):
        days_in_month = 30
    elif month == 2:
        if is_leap:
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        days_in_month = 31

    if day >= 1 and day <= days_in_month:
        print("var")
    else:
        print("yoxdur")