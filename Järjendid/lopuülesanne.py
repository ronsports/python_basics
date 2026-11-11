nimed = []
punktid = []

with open("kontrolltoo.csv", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.strip().split(";")
        nimed.append(osad[0])
        punktid.append(int(osad[1]))

print("KONTROLLTÖÖ TULEMUSED")
for i in range(len(nimed)):
    print(f"{i + 1}. {nimed[i]} – {punktid[i]} punkti")

opilaste_arv = len(nimed)
summa = 0
for p in punktid:
    summa = summa + p
keskmine = summa / opilaste_arv

suurim_punkt = punktid[0]
vaikseim_punkt = punktid[0]

for p in punktid:
    if p > suurim_punkt:
        suurim_punkt = p
    if p < vaikseim_punkt:
        vaikseim_punkt = p

parimad_opilased = []
halvimad_opilased = []

for i in range(len(punktid)):
    if punktid[i] == suurim_punkt:
        parimad_opilased.append(nimed[i])
    if punktid[i] == vaikseim_punkt:
        halvimad_opilased.append(nimed[i])

vahemalt_50 = 0
alla_50 = 0
for p in punktid:
    if p >= 50:
        vahemalt_50 = vahemalt_50 + 1
    else:
        alla_50 = alla_50 + 1

print("\nSTATISTIKA")
print("Õpilaste koguarv:", opilaste_arv)
print("Keskmine punktisumma:", round(keskmine, 2))
print("Suurim punktisumma:", suurim_punkt, "Õpilane/Õpilased:", ", ".join(parimad_opilased))
print("Väikseim punktisumma:", vaikseim_punkt, "Õpilane/Õpilased:", ", ".join(halvimad_opilased))
print("Õpilaste arv, kes said vähemalt 50 punkti:", vahemalt_50)
print("Õpilaste arv, kes said alla 50 punkti:", alla_50)

print("\nHINDED")
for i in range(len(nimed)):
    p = punktid[i]
    if p >= 90:
        hinne = 5
    elif p >= 75:
        hinne = 4
    elif p >= 50:
        hinne = 3
    elif p >= 20:
        hinne = 2
    else:
        hinne = 1
    print(f"{nimed[i]} – {p} punkti – hinne {hinne}")

print("\nÕPILASE OTSIMINE")
küsimus = input("Sisesta õpilase nimi: ")

leitud = False
for i in range(len(nimed)):
    if nimed[i].lower() == küsimus.lower():
        p = punktid[i]
        if p >= 90:
            hinne = 5
        elif p >= 75:
            hinne = 4
        elif p >= 50:
            hinne = 3
        elif p >= 20:
            hinne = 2
        else:
            hinne = 1
        
        print("Õpilane:", nimed[i])
        print("Punktid:", p)
        print("Hinne:", hinne)
        leitud = True

if not leitud:
    print("Sellist õpilast ei leitud.")
