x = float(input("x yazin: "))
y = float(input("y yazin: "))

point = (x, y)

x, y = point

if x == 0 and y == 0:
    print("Noqte merkezdedir (0, 0)")
elif x == 0:
    print("Noqte Y oxunun uzerindedir")
elif y == 0:
    print("Noqte X oxunun uzerindedir")
elif x > 0 and y > 0:
    print("I rub")
elif x < 0 and y > 0:
    print("II rub")
elif x < 0 and y < 0:
    print("III rub")
else:
    print("IV rub")