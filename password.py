password = input("Şifreni yazin: ")

has_length = len(password) >= 8
has_upper = password.lower() != password
has_lower = password.upper() != password
not_only_letters = not password.isalpha()

if not has_length:
    print("Zeif")
elif has_upper and has_lower and not_only_letters:
    print("Guclu")
else:
    print("Orta")