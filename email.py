email = input("Email yazin: ")

if " " in email:
    print("Sehvdir: bosluq olmamalidir")
elif email.count("@") != 1:
    print("Sehvdir: tam 1 dene @ olmaliidir")
else:
    username, domain = email.split("@")
if "." not in domain:
        print("Sehvdir: domendə en azi bir nöqte (.) olmalidir")
else:
        print("Username:", username)
        print("Domen:", domain)