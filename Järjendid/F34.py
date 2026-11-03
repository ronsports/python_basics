muugid = [125.50, 210.00, 98.75, 340.20, 185.40, 420.00, 275.90]
paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]

kogumuuk = sum(muugid)
keskmine = kogumuuk / len(muugid)

suurim_muuk = muugid[0]
suurim_paev = paevad[0]

yle_200_paevi = 0

print("Nädala müügitulemused:")
for i in range(len(muugid)):
    print(f"{paevad[i]}: {muugid[i]:.2f} €")
    
    if muugid[i] > suurim_muuk:
        suurim_muuk = muugid[i]
        suurim_paev = paevad[i]
        
    if muugid[i] > 200:
        yle_200_paevi = yle_200_paevi + 1

print(f"\nNädala kogumüük: {kogumuuk:.2f} €")
print(f"Keskmine päevamüük: {keskmine:.2f} €")
print(f"Suurima müügiga päev: {suurim_paev} ({suurim_muuk:.2f} €)")
print(f"Päevi, mil müük ületas 200 €: {yle_200_paevi}")
