koik_keskmised = []
aruanne_read = []

with open("õpilased.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) > 1:
            nimi = osad[0]
            
            # Teisendame kõik ülejäänud osad hinnete täisarvudeks
            hinded = []
            for h in osad[1:]:
                hinded.append(int(h))
            
            if len(hinded) > 0:
                opilase_keskmine = sum(hinded) / len(hinded)
                koik_keskmised.append(opilase_keskmine)
                aruanne_read.append(f"{nimi}: {opilase_keskmine:.2f}")

# Arvutame klassi keskmise hinde
if len(koik_keskmised) > 0:
    klassi_keskmine = sum(koik_keskmised) / len(koik_keskmised)
else:
    klassi_keskmine = 0.0

# Koostame lõpliku aruande teksti
aruanne_tekst = "--- ÕPILASTE TULEMUSTE ARUANNE ---\n"
for rida in aruanne_read:
    aruanne_tekst = aruanne_tekst + rida + "\n"

aruanne_tekst = aruanne_tekst + "----------------------------------\n"
aruanne_tekst = aruanne_tekst + f"Kogu klassi keskmine hinne: {klassi_keskmine:.2f}\n"

# Kuvame aruande terminalis
print(aruanne_tekst)

# Salvestame tulemuse faili
with open("opilaste_aruanne.txt", "w", encoding="utf-8") as valjund:
    valjund.write(aruanne_tekst)