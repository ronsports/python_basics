kogu_tulu = 0.0
suurim_tulu = -1.0
suurim_toode = ""
toodete_read = []

with open("muuk.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) == 3:
            nimi = osad[0]
            hind = float(osad[1])
            kogus = int(osad[2])
            
            tulu = hind * kogus
            kogu_tulu = kogu_tulu + tulu
            
            toodete_read.append(f"{nimi}: {tulu:.2f} €")
            
            if tulu > suurim_tulu:
                suurim_tulu = tulu
                suurim_toode = nimi

# Koostame aruande teksti
aruanne = "--- MÜÜGIARUANNE ---\n"
for toode_rida in toodete_read:
    aruanne = aruanne + toode_rida + "\n"

aruanne = aruanne + "--------------------\n"
aruanne = aruanne + f"Kogu müügitulu: {kogu_tulu:.2f} €\n"
aruanne = aruanne + f"Suurima müügituluga toode: {suurim_toode} ({suurim_tulu:.2f} €)\n"

# Kuvame aruande terminalis
print(aruanne)

# Salvestame aruande faili
with open("muugiaruanne.txt", "w", encoding="utf-8") as valjund:
    valjund.write(aruanne)
