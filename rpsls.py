beats = {
    "qayçi": ("kagiz", "kertenkele"),
    "kagz": ("das", "spok"),
    "das": ("kertenkele", "qayci"),
    "kertenkele": ("spok", "kagiz"),
    "spok": ("qayci", "das"),
}

player1 = input("1-ci oyuncu secimi: ").lower()
player2 = input("2-ci oyuncu secimi: ").lower()

if player1 not in beats or player2 not in beats:
    print("Bele secim yoxdur")
elif player1 == player2:
    print("Hec-hece")
elif player2 in beats[player1]:
    print("1-ci oyuncu qalibdir")
else:
    print("2-ci oyuncu qalibdir")