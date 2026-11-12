nimed = ["Mari", "Jaan", "Kati"]
punktid = [87, 64, 95]

def arvuta_hinne(p):
    if p >= 90:
        return 5
    elif p >= 75:
        return 4
    elif p >= 50:
        return 3
    elif p >= 20:
        return 2
    else:
        return 1

def lisa_opilane(nimed, punktid, nimi, tulemus):
    for olemasolev in nimed:
        if olemasolev.lower() == nimi.lower():
            print("Viga: sellise nimega õpilane on juba olemas!")
            return False
    nimed.append(nimi)
    punktid.append(tulemus)
    return True

def leia_keskmine(punktid):
    return sum(punktid) / len(punktid)

def leia_parim(nimed, punktid):
    i = punktid.index(max(punktid))
    return nimed[i], punktid[i]

def leia_norgim(nimed, punktid):
    i = punktid.index(min(punktid))
    return nimed[i], punktid[i]

def kuva_opilased(nimed, punktid, pealkiri="--- ÕPILASTE NIMEKIRI ---"):
    print(pealkiri)
    if len(nimed) == 0:
        print("Õpilaste nimekiri on tühi.")
        return
    for i in range(len(nimed)):
        p = punktid[i]
        hinne = arvuta_hinne(p)
        print(f"{nimed[i]}: {p} punkti, hinne {hinne}")

def kuva_statistika(nimed, punktid):
    if len(nimed) == 0:
        print("Statistikat ei saa kuvada, õpilaste nimekiri on tühi.")
        return
    p_nimi, p_skoor = leia_parim(nimed, punktid)
    n_nimi, n_skoor = leia_norgim(nimed, punktid)
    print(f"Õpilaste arv: {len(nimed)}")
    print(f"Klassi keskmine: {round(leia_keskmine(punktid), 1)}")
    print(f"Parim õpilane: {p_nimi} ({p_skoor} p)")
    print(f"Nõrgim õpilane: {n_nimi} ({n_skoor} p)")
    
    print("Hinnete jaotus:")
    for h in range(5, 0, -1):
        kogus = 0
        for p in punktid:
            if arvuta_hinne(p) == h:
                kogus += 1
        print(f"Hinne {h}: {kogus} õpilast")

def otsi_opilane(nimed, punktid, nimi):
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():
            return nimed[i], punktid[i]
    return None

def kuva_menuu():
    print("\n--- MENÜÜ ---")
    print("1. Lisa õpilane")
    print("2. Kuva kõik õpilased")
    print("3. Kuva klassi statistika")
    print("4. Otsi õpilast nime järgi")
    print("5. Lõpeta programm")

while True:
    kuva_menuu()
    valik = input("Vali tegevus (1-5): ")
    
    if valik == "1":
        nimi = input("Sisesta õpilase nimi: ").strip()
        if nimi == "":
            print("Viga: nimi ei tohi olla tühi.")
            continue
        try:
            tulemus = int(input("Sisesta punktisumma (0-100): "))
            if tulemus < 0 or tulemus > 100:
                print("Viga: punktisumma peab olema vahemikus 0-100.")
            else:
                if lisa_opilane(nimed, punktid, nimi, tulemus):
                    print("Õpilane lisatud!")
        except ValueError:
            print("Viga: palun sisesta täisarv.")
    elif valik == "2":
        kuva_opilased(nimed, punktid)
    elif valik == "3":
        print("--- STATISTIKA ---")
        kuva_statistika(nimed, punktid)
    elif valik == "4":
        if len(nimed) == 0:
            print("Õpilaste nimekiri on tühi.")
        else:
            tulemus = otsi_opilane(nimed, punktid, input("Sisesta otsitav nimi: ").strip())
            if tulemus:
                hinne = arvuta_hinne(tulemus[1])
                print(f"Leitud: {tulemus[0]} - {tulemus[1]} punkti (hinne {hinne})")
            else:
                print("Sellist õpilast ei leitud.")
    elif valik == "5":
        print("Programmi lõpp.")
        break
    else:
        print("Viga: palun vali tegevus vahemikus 1-5.")
