cart = []


cart.append("çörək")
cart.append("süd")
cart.append("alma")
cart.append("pendir")
print("Səbət:", cart)


cart.remove("süd")
print("Süd silindikdən sonra:", cart)

product = input("Məhsul adi yazin: ")

if product in cart:
    print("Bu məhsul səbətdə var")
else:
    print("Bu məhsul səbətdə yoxdur")


print("Əlifba sirasi ilə:", sorted(cart))


print("Məhsul sayi:", len(cart))