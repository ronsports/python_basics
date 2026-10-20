nimed = ["Mari", "Jaan", "Kati"]
punktid = [87, 64, 95]

def lisa_opilane(nimed, punktid, nimi, tulemus):
    nimed.append(nimi)
    punktid.append(tulemus)

def leia_keskmine(punktid):
    return sum(punktid) / len(punktid)

def leia_parim(nimed, punktid):
    i = punktid.index(max(punktid))
    return nimed[i], punktid[i]

def leia_norgim(nimed, punktid):
    i = punktid.index(min(punktid))
    return nimed[i], punktid[i]

def kuva_opilased(nimed, punktid):
    for i in range(len(nimed)):
        p = punktid[i]
        hinne = 5 if p >= 90 else 4 if p >= 75 else 3 if p >= 50 else 2
        print(f"{nimed[i]}: {p} punkti, hinne {hinne}")

def kuva_statistika(nimed, punktid):
    p_nimi, p_skoor = leia_parim(nimed, punktid)
    n_nimi, n_skoor = leia_norgim(nimed, punktid)
    print(f"Õpilaste arv: {len(nimed)}")
    print(f"Klassi keskmine: {round(leia_keskmine(punktid), 1)}")
    print(f"Parim õpilane: {p_nimi} ({p_skoor} p)")
    print(f"Nõrgim õpilane: {n_nimi} ({n_skoor} p)")

def otsi_opilane(nimed, punktid, nimi):
    if nimi in nimed:
        i = nimed.index(nimi)
        return nimed[i], punktid[i]
    return None

def kuva_menuu():
    print(" MENÜÜ ---1. Lisa õpilane 2. Kuva kõik õpilased 3. Kuva klassi statistika 4. Otsi õpilast nime järgi 5. Lõpeta programm")

while True:
    kuva_menuu()
    valik = input("Vali tegevus (1-5): ")
    
    if valik == "1":
        lisa_opilane(nimed, punktid, input("Sisesta õpilase nimi: "), int(input("Sisesta punktisumma: ")))
        print("Õpilane lisatud!")
    elif valik == "2":
        print("--- ÕPILASTE NIMEKIRI ---")
        kuva_opilased(nimed, punktid)
    elif valik == "3":
        print("--- STATISTIKA ---")
        kuva_statistika(nimed, punktid)
    elif valik == "4":
        tulemus = otsi_opilane(nimed, punktid, input("Sisesta otsitav nimi: "))
        print(f"Leitud: {tulemus[0]} - {tulemus[1]} punkti" if tulemus else "Sellist õpilast ei leitud.")
    elif valik == "5":
        print("Programmi lõpp.")
        break
    else:
        print("error")
