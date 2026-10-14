küsimus = input("Kasutajanimi: ")

if not (5 <= len(küsimus) <= 15):
    print("Viga: kasutajanime pikkus peab olema 5–15 tähemärki.")
elif not küsimus.isalnum():
    print("Viga: kasutajanimi tohib sisaldada ainult ladina tähti ja numbreid.")
elif not küsimus[0].isalpha():
    print("Viga: kasutajanimi peab algama tähega.")
else:
    print("Kasutajanimi sobib.")