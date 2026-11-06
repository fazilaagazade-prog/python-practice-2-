scores = [78, 92, 65, 88, 100, 54, 91, 73]

print("En yuksek bal:", max(scores))
print("En asagi bal:", min(scores))
print("Netice sayi:", len(scores))
print("Siralanmis siyahi:", sorted(scores))
print("En yaxsi 3 netice:", sorted(scores, reverse=True)[:3])

score = int(input("Bal yazin: "))

if score in scores:
    print("Bu bal siyahida var")
else:
    print("Bu bal siyahida yoxdur")