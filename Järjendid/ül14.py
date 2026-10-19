sonad = ["Python", "programmeerimine", "järjend", "tsükkel", "fail"]

for sona in sonad:
    pikkus = len(sona)
    esimene_taht = sona[0]
    viimane_taht = sona[-1]
    print(f"{sona} – {pikkus} tähemärki (esimene: {esimene_taht}, viimane: {viimane_taht})")
