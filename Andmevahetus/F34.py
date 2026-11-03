failinimi = "hinded.txt"

while True:
    print("\n1. Kuva | 2. Lisa | 3. Otsi | 4. Statistika | 5. Salvesta | 6. Lõpeta")
    valik = input("Vali tegevus (1-6): ").strip()

    if valik == "1":
        with open(failinimi, "r", encoding="utf-8") as f:
            print(f.read().strip())

    elif valik == "2":
        nimi = input("Õpilase nimi: ")
        hinne = input("Hinne (1-5): ")
        with open(failinimi, "a", encoding="utf-8") as f:
            f.write(f"{nimi} {hinne}\n")

    elif valik == "3":
        otsi = input("Keda otsid? ").lower()
        with open(failinimi, "r", encoding="utf-8") as f:
            for rida in f:
                if otsi in rida.lower():
                    print(rida.strip())

    elif valik == "4" or valik == "5":
        summa, kogus = 0, 0
        jaotus = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        with open(failinimi, "r", encoding="utf-8") as f:
            for rida in f:
                osad = rida.split()
                if len(osad) >= 2:
                    h = int(osad[-1])
                    summa += h
                    kogus += 1
                    jaotus[h] += 1

        keskmine = summa / kogus if kogus > 0 else 0
        tulemus = f"Klassi keskmine: {keskmine:.2f}\n"
        for h in range(1, 6):
            tulemus += f"Hinne {h}: {'*' * jaotus[h]}\n"

        if valik == "4":
            print("\n" + tulemus)
        else:
            with open("hinnete_aruanne.txt", "w", encoding="utf-8") as f:
                f.write(tulemus)
            print("Aruanne salvestatud!")

    elif valik == "6":
        print("Head aega!")
        break
