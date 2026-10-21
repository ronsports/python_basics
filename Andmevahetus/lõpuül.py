import os

if not os.path.exists("tulemused.txt"):
    print("Viga: Faili 'tulemused.txt' ei leitud!")
else:
    fail = open("tulemused.txt", "r", encoding="utf-8")
    read = fail.readlines()
    fail.close()

    valjund = "õpilaste tulemus"
    
    summa_keskmised = 0
    parim_tulemus = -1
    norgim_tulemus = 101
    parim_nimi = ""
    norgim_nimi = ""
    positiivsed = 0

    for rida in read:
        t = rida.strip().split(";")
        nimi = t[0]
        keskmine = (int(t[1]) + int(t[2]) + int(t[3])) / 3
        
        if keskmine >= 90: hinne = 5
        elif keskmine >= 75: hinne = 4
        elif keskmine >= 60: hinne = 3
        elif keskmine >= 50: hinne = 2
        else: hinne = 1

        if hinne >= 3:
            positiivsed += 1

        summa_keskmised += keskmine

        if keskmine > parim_tulemus:
            parim_tulemus = keskmine
            parim_nimi = nimi
        if keskmine < norgim_tulemus:
            norgim_tulemus = keskmine
            norgim_nimi = nimi

        valjund += f"{nimi:<10} Keskmine: {keskmine:.2f}  Hinne: {hinne}\n"

    klassi_keskmine = summa_keskmised / len(read)
    
    valjund += "------------------------------\n"
    valjund += f"klassi keskmine: {klassi_keskmine:.2f}\n"
    valjund += f"parim õpilane: {parim_nimi}\n"
    valjund += f"nõrgim õpilane: {norgim_nimi}\n"
    valjund += f"positiivse hindega õpilasi: {positiivsed}\n"

    print(valjund, end="")

    fail_aruanne = open("aruanne.txt", "w", encoding="utf-8")
    fail_aruanne.write(valjund)
    fail_aruanne.close()
