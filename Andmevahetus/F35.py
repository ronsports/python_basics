failinimi = input("Sisesta faili nimi: ")

with open(failinimi, "r", encoding="utf-8") as f:
    tekst = f.read()

sonad = tekst.split()
lausete_arv = tekst.count(".") + tekst.count("?") + tekst.count("!")

pikim_sona = ""
sagedused = {}

for s in sonad:
    puhas = s.strip(".,!?;:()\"'").lower()
    if len(puhas) > 0:
        if len(puhas) > len(pikim_sona):
            pikim_sona = puhas
        sagedused[puhas] = sagedused.get(puhas, 0) + 1

top_sonad = sorted(sagedused.items(), key=lambda x: x[1], reverse=True)[:5]

aruanne = f"Sõnu: {len(sonad)}\nLauseid: {lausete_arv}\nPikim sõna: {pikim_sona}\nTop 5 sõnad:\n"
for sona, arv in top_sonad:
    aruanne += f"- {sona}: {arv}\n"

print("\n" + aruanne)

with open("tekstianaluus.txt", "w", encoding="utf-8") as f:
    f.write(aruanne)
